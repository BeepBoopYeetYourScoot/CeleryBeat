from django.db import models


class ProductOffer(models.Model):
    """
    Insert fields here
    """
    scallium_id = models.UUIDField()
    sellable = models.BooleanField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_offers'
        ordering = ['scallium_id']


class ProductOfferAvailabilities(models.Model):
    offer = models.ForeignKey(ProductOffer,
                              on_delete=models.SET_NULL,
                              null=True)
    value = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'product_offer_availabilities'
        default_related_name = 'availabilities'


class ProductOfferPrice(models.Model):
    offer = models.ForeignKey(ProductOffer,
                              on_delete=models.SET_NULL,
                              null=True)
    value = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'product_offer_prices'
        default_related_name = 'prices'


class ProductOfferQuantities(models.Model):
    offer = models.ForeignKey(ProductOffer,
                              on_delete=models.SET_NULL,
                              null=True)

    class Meta:
        managed = False
        db_table = 'product_offer_quantities'
        default_related_name = 'quantities'
