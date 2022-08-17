from django.conf import settings
from django.db import models
from django.db.models.deletion import SET

from .album import Album
from .user import User


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Track(models.Model):
    album = models.ForeignKey(Album, related_name="track", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    audio_file = models.FileField(upload_to="track", default=settings.MEDIA_ROOT + "/track/track.mp3")
    liked_by = models.ManyToManyField(User, through="TrackLikes")

    track_length = models.DurationField()
    explicit_content = models.BooleanField(default=False)

    writer = models.CharField()
    composer = models.CharField()
    producer = models.CharField()
    lyrics = models.TextField()

    def __str__(self) -> str:
        return self.track_title


class TrackLikes(models.Model):
    liked_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    track = models.ForeignKey(to=Track, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("track", "liked_by")
