from django.db import models

from .artist import Artist
from .models import Track
from .playlist import Playlist
from .user import User


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    created_by_artist = models.ForeignKey(to=Artist, null=True)
    created_by_user = models.ForeignKey(to=User, null=True)
    description = models.CharField(max_length=5000)
    liked_by = models.ManyToManyField(User, through="PlaylistLikes")
    type = models.CharField(max_length=4, choices=[("")])
    track = models.ManyToManyField(Track, through="PlaylistContent")
    participant = models.ManyToManyField(User, through="PlaylistParticipants")
    visibility = models.CharField(
        max_length=4, choices=[("PB", "public"), ("PR", "private"), ("FW", "followers"), ("FR", "friends")]
    )


class PlaylistLikes(models.Model):
    liked_by = models.ForeignKey(to=User)
    playlist = models.ForeignKey(to=Playlist)


class PlaylistContent(models.Model):
    track = models.ForeignKey(to=Track)
    added_by = models.ForeignKey(to=User, null=True)
    playlist = models.ForeignKey(to=Playlist)

    class Meta:
        unique_together = ("track", "added_by")


class PlaylistParticipants(models.Model):
    playlist = models.ForeignKey(to=Playlist)
    participant = models.ForeignKey(to=User)
