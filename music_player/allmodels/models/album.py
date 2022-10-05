from django.conf import settings
from django.db import models

from .artist import Artist
from .location import Country
from .not_req_user import User


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = "Genre"


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name="album_artist", on_delete=models.CASCADE)  # cascade
    genre = models.ForeignKey(Genre, related_name="album_genre", on_delete=models.CASCADE)
    album_title = models.CharField(max_length=50)
    album_logo = models.FileField(upload_to="album", default=settings.MEDIA_ROOT + "/album_art/default.png")
    liked_by = models.ManyToManyField(User, through="AlbumLikes")

    def __str__(self) -> str:
        return self.album_title + " - " + self.artist.name
    class Meta:
        db_table = "Album"


class AlbumReleaseInfo(models.Model):
    album = models.ForeignKey(Album, null=False, blank=False, on_delete=models.CASCADE, related_name="related3")
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE, related_name="related4")
    date = models.DateField()

    class Meta:
        unique_together = ("album", "country")
        db_table = "AlbumReleaseInfo"



class AlbumLikes(models.Model):
    liked_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="related5")
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE, related_name="related6")

    class Meta:
        unique_together = ("album", "liked_by")
        db_table = "AlbumLikes"
