from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from .artist import Artist
from .user import User


class ArtistManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("Users must have a username")

        if email is None:
            raise TypeError("User must have an email address")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


class Artist(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = ArtistManager()

    def __str__(self) -> str:
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username.split()[0]


class Followers(models.Model):
    followed_by = models.ForeignKey(to=User)
    artist = models.ForeignKey(to=Artist)

    class Meta:
        unique_together = ("artist", "followed_by")
