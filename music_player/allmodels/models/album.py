from django.conf import settings
from django.db import models
from django.db.models.deletion import SET

from .artist import Artist
from .models import Genre


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name="album_artist", on_delete=SET(1))
    genre = models.ForeignKey(Genre, related_name="album_genre", on_delete=SET(1))
    album_title = models.CharField(max_length=500)
    album_logo = models.FileField(upload_to="album", default=settings.MEDIA_ROOT + "/album_art/default.png")

    def __str__(self) -> str:
        return self.album_title + " - " + self.artist.name
