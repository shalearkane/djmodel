from django.conf import settings
from django.db import models
from django.db.models.deletion import SET

from .artist import Artist
from .others import Genre
from .user import User


class Country(models.Model):
    name = models.CharField(unique=True)


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name="album_artist", on_delete=models.CASCADE)  # cascade
    genre = models.ForeignKey(Genre, related_name="album_genre", on_delete=models.CASCADE)
    album_title = models.CharField(max_length=500)
    album_logo = models.FileField(upload_to="album", default=settings.MEDIA_ROOT + "/album_art/default.png")
    liked_by = models.ManyToManyField(User, through="AlbumLikes")

    def __str__(self) -> str:
        return self.album_title + " - " + self.artist.name


class AlbumReleaseInfo(models.Model):
    album = models.ForeignKey(Album, null=False, blank=False, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ("album", "country")


class AlbumLikes(models.Model):
    liked_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("album", "liked_by")
