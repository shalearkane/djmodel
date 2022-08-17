from django.db import models
from django.conf import settings

class RecordLabel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    record_label_logo = models.FileField(upload_to="record_label", default=settings.MEDIA_ROOT + "/album_art/default.png")

    def __str__(self) -> str:
        return self.name