from django.db import models

from .album import Album


class Promotions(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    album = models.ForeignKey(Album, related_name="SIXTYNINE", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Promotions"


class BusinessAgreement(models.Model):
    promotion_fees = models.IntegerField()
    royalty_fees = models.DecimalField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = "BusinessAgreement"

