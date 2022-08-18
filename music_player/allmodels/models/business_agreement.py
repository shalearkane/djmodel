from django.db import models
from .album import Album


class Promotions(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    album=models.ForeignKey(Album,related_name='SIXTYNINE',on_delete=models.CASCADE)


class BuissnessAgreement(models.Model):
    promotion_fees=models.IntegerField()
    royalty_fees=models.DecimalField()
    start_date = models.DateField()
    end_date = models.DateField()

