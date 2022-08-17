from django.conf import settings
from django.db import models

from .artist import Artist


class Event(models.Model):
    artist = models.ForeignKey(to=Artist)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField()
    registration = models.URLField()
    event_poster = models.FileField(upload_to="album", default=settings.MEDIA_ROOT + "/event_poster/default.png")
