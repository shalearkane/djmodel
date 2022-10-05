from django.db import models

from .not_req_user import User


class Friendship(models.Model):
    friendship_from = models.ForeignKey(User, related_name="friendship_from")
    friendship_to = models.ForeignKey(User, related_name="friendship_to")

    class Meta:
        db_table = "Friendship"
