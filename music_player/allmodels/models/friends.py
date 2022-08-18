from django.db import models
from .user import User
class Friendship(models.Model):
    friendship_from = models.ForeignKey(User, related_name="friendship_from")
    friendship_to = models.ForeignKey(User, related_name="friendship_to")
