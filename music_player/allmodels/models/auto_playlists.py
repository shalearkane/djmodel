from django.db import models
from django.db.models.deletion import CASCADE

from .others import Track
from .user import User


class LikedSong(models.Model):
    user = models.ForeignKey(User, related_name="user_like", on_delete=CASCADE)
    track = models.ForeignKey(Track, related_name="liked_track", on_delete=CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "track")

    def __str__(self) -> str:
        return self.user.username + " - " + self.track.track_title


class History(models.Model):
    user = models.ForeignKey(User, related_name="user_listened", on_delete=CASCADE)
    track = models.ForeignKey(Track, related_name="listened_track", on_delete=CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username + " - " + self.track.track_title
