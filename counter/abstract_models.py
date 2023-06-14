from django.db import models


class AbstractComparisonResult(models.Model):
    offer_id = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)

    class Meta:
        abstract = True
