from django.db import models

from .album import Genre
from .location import Country
from .user import User


class Podcast(models.Model):
    host = models.ForeignKey(User, related_name="podcast_host", on_delete=models.CASCADE)  # cascade
    genre = models.ForeignKey(Genre, related_name="album_genre", on_delete=models.CASCADE)
    podcast_title = models.CharField(max_length=50)
    # album_logo = models.FileField(upload_to="album", default=settings.MEDIA_ROOT + "/album_art/default.png")
    guest = models.CharField(max_length=50)
    bookmarked_by = models.ManyToManyField(User, through="PoscastBookmarks")

    def __str__(self) -> str:
        return self.host + " - " + self.host


class PoscastBookmarks(models.Model):
    liked_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="related101")
    podcast = models.ForeignKey(to=Podcast, on_delete=models.CASCADE, related_name="related102")

    class Meta:
        unique_together = ("podcast", "liked_by")


class PodcastReleaseInfo(models.Model):
    podcast = models.ForeignKey(Podcast, null=False, blank=False, on_delete=models.CASCADE, related_name="related103")
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE, related_name="related104")
    date = models.DateField()
    nationality = models.ForeignKey(Country, null=False, on_delete=models.CASCADE, related_name="related105")

    class Meta:
        unique_together = ("podcast", "country")
