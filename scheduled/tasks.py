from celery import shared_task
from django_celery_beat.models import IntervalSchedule, \
    PeriodicTask

from counter.models import ComparisonResult, RMComparisonResult, \
    M2ComparisonResult
from integrations.models.m2_models import Offer
from integrations.models.rm_models import ProductOffer


@shared_task(bind=False, name='scheduled.compare_offers')
def compare_offers(m2_offer_model=Offer, rm_offer_model=ProductOffer):
    m2_offers_ids = m2_offer_model.objects.values_list('scallium_id',
                                                       flat=True)
    rm_offer_ids = rm_offer_model.objects.values_list('scallium_id', flat=True)
    mutual, m2_only, rm_only = split_offers(m2_offers_ids, rm_offer_ids)

    mutual_m2 = Offer.objects.filter(scallium_id__in=mutual)
    mutual_rm = ProductOffer.objects.filter(
        scallium_id__in=mutual).prefetch_related(
        'availabilities',
        'prices',
        'quantities',
    )
    assert mutual_m2.count() == mutual_rm.count()
    for m2_offer, rm_offer in zip(mutual_m2, mutual_rm):
        if not rm_offer.sellable:
            rm_result = RMComparisonResult.objects.create(
                offer_id=rm_offer.id,
                sellable=rm_offer.sellable,
            )
            comparison = ComparisonResult.objects.create(
                m2_result=None,
                rm_result=rm_result,
                reason='SELLABILITY',
            )
            print(comparison)

        if m2_offer.is_moderated:
            m2_result = M2ComparisonResult.objects.create(
                offer_id=m2_offer.id,
                in_moderation=m2_offer.is_moderated,
            )
            comparison = ComparisonResult.objects.create(
                m2_result=m2_result,
                rm_result=None,
                reason='MODERATION',
            )
            print(comparison)

        eq_quantity = (rm_offer.quantities.count() == 1
                       and
                       m2_offer.quantity == rm_offer.quantities.all()[0].value)
        eq_price = (mutual_rm.prices.count() == 1
                    and
                    m2_offer.price == rm_offer.prices.all()[0].value)
        if not (eq_quantity and eq_price):
            m2_result = M2ComparisonResult.objects.create(
                offer_id=m2_offer.id,
                quantity=m2_offer.quantity,
                price=m2_offer.price,
            )
            rm_result = RMComparisonResult.objects.create(
                offer_id=rm_offer.id,
                quantity=rm_offer.quantities.latest('id'),
                price=rm_offer.prices.latest('id'),
                quantity_count=rm_offer.quantities.count(),
                price_count=rm_offer.prices.count(),
            )
            comparison = ComparisonResult.objects.create(
                m2_result=m2_result,
                rm_result=rm_result,
                reason='UNMATCH'
            )
            print(comparison)


def split_offers(m2_offer_ids: list, rm_offer_ids: list) -> tuple:
    m2_only_offers = [idx for idx in m2_offer_ids if idx not in rm_offer_ids]
    rm_only_offers = [idx for idx in rm_offer_ids if idx not in m2_offer_ids]
    mutual_offers = [idx for idx in m2_offer_ids if idx not in m2_only_offers]
    return mutual_offers, m2_only_offers, rm_only_offers


schedule, created = IntervalSchedule.objects.get_or_create(
    every=3,
    period=IntervalSchedule.HOURS,
)

comparison_task = PeriodicTask.objects.get_or_create(
    interval=schedule,
    name='Comparison task',
    task='scheduled.compare_offers',
)[0]
