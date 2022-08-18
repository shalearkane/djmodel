from django.db import models
from django.db.models.deletion import CASCADE

from .user import User


class SubscriptionInfo(models.Model):
    user = models.ForeignKey(to=User)
    method = models.CharField(
        max_length=4, choices=(("DC", "Debit Card"), ("CC", "Credit Card"), ("PC", "Promo Code"), ("UPI", "UPI"))
    )
    transaction_id = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Subscription(models.Model):
    user = models.ForeignKey(to=User, related_name="subs_use", on_delete=CASCADE)
    type = models.CharField(
        max_length=4, choices=(("FM", "FamilyPack"), ("IN", "Individual"), ("CP", "Couple"), ("ST", "Student"))
    )
    transcation_info = models.ForeignKey(to=SubscriptionInfo)
