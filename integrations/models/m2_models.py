from django.db import models


class Offer(models.Model):
    """
    Insert fields here
    """
    scallium_id = models.UUIDField()
    is_moderated = models.BooleanField()
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'offers'
        ordering = ['scallium_id']
