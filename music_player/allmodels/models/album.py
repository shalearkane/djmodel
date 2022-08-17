from django.conf import settings
from django.db import models

from .artist import Artist
from .user import User


class Country(models.Model):
    name = models.CharField(unique=True, max_length=30)


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name="album_artist", on_delete=models.CASCADE, related_name='1')  # cascade
    genre = models.ForeignKey(Genre, related_name="album_genre", on_delete=models.CASCADE, related_name='2')
    album_title = models.CharField(max_length=50)
    album_logo = models.FileField(upload_to="album", default=settings.MEDIA_ROOT + "/album_art/default.png")
    liked_by = models.ManyToManyField(User, through="AlbumLikes")

    def __str__(self) -> str:
        return self.album_title + " - " + self.artist.name


class AlbumReleaseInfo(models.Model):
    album = models.ForeignKey(Album, null=False, blank=False, on_delete=models.CASCADE, related_name='3')
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE, related_name='4')
    date = models.DateField()

    class Meta:
        unique_together = ("album", "country")


class AlbumLikes(models.Model):
    liked_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='5')
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE, related_name='6')

    class Meta:
        unique_together = ("album", "liked_by")
