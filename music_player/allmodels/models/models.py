from django.conf import settings
from django.db import models
from django.db.models.deletion import SET

from .album import Album


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Track(models.Model):
    album = models.ForeignKey(Album, related_name="track", on_delete=SET(1))
    track_title = models.CharField(max_length=250)
    audio_file = models.FileField(upload_to="track", default=settings.MEDIA_ROOT + "/track/track.mp3")

    def __str__(self) -> str:
        return self.track_title