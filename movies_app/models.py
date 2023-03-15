from django.db import models
from django.db.models import RESTRICT


class Director(models.Model):

    class Meta:
        db_table = 'directors'

    name = models.CharField(null=False, blank=False, db_column='name', db_index=True, max_length=128)
    birth_date = models.DateField()


# Create your models here.
class Movie(models.Model):

    # https://docs.djangoproject.com/en/4.1/ref/models/options/
    class Meta:
        db_table = 'movies'

    name = models.CharField(null=False, blank=False, db_column='name', db_index=True, max_length=128)
    year = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    poster_url = models.CharField(null=True, blank=True, max_length=256)
    director = models.ForeignKey(to=Director, on_delete=RESTRICT, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"




