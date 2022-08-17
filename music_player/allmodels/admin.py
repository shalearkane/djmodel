# Register your models here.
from django.contrib import admin

from .models.album import Album

admin.site.register(Album)
