from django.db import models

from .record_label import RecordLabel
from .user import User


class Artist(models.Model):
    username = models.CharField(db_index=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    record_label = models.ForeignKey(RecordLabel, null=False, on_delete=models.CASCADE, related_name='10')
    password = models.CharField(max_length=30)

    about = models.TextField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.

    def __str__(self) -> str:
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username.split()[0]


class ArtistPhotos(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='7')
    photo = models.FileField()
    date_added = models.DateField(auto_now_add=True)


class Followers(models.Model):
    followed_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='8')
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE, related_name='9')

    class Meta:
        unique_together = ("artist", "followed_by")
