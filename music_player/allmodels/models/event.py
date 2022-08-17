from django.db import models
from .artist import Artist
from .user import User

class Event(models.Model):
    artist = models.ForeignKey(to=Artist)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField()
