from django.conf import settings
from django.db import models


class RecordLabel(models.Model):
    username = models.CharField(db_index=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    record_label_logo = models.FileField(upload_to="record_label", default=settings.MEDIA_ROOT + "/rl_logo/default.png")

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
