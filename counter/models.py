from django.db import models

from counter.abstract_models import AbstractComparisonResult


class M2ComparisonResult(AbstractComparisonResult):
    in_moderation = models.BooleanField(default=False)


class RMComparisonResult(AbstractComparisonResult):
    sellable = models.BooleanField(default=True)
    quantity_count = models.PositiveIntegerField(null=True)
    price_count = models.PositiveIntegerField(null=True)


class ComparisonResult(models.Model):
    REASONS = (
        ('UNMATCH', 'Не прошёл сравнение состояний'),
        ('MODERATION', 'Находится на модерации в М2'),
        ('SELLABILITY', 'sellable=false в базе RM'),
    )

    m2_result = models.OneToOneField(M2ComparisonResult,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     )
    rm_result = models.OneToOneField(RMComparisonResult,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     )

    reason = models.CharField(max_length=256, choices=REASONS)
    checked_at = models.DateTimeField(auto_now_add=True)

