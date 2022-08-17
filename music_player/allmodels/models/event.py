from django.db import models

from .artist import Artist


class Event(models.Model):
    artist = models.ForeignKey(to=Artist)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField()
