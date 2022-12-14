from django.db import models


class Country(models.Model):
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        db_table = "Country"
