from django.db import models
from django.db.models import RESTRICT


class Director(models.Model):

    class Meta:
        db_table = 'directors'

    name = models.CharField(null=False, blank=False, db_column='name', db_index=True, max_length=128)
    birth_date = models.DateField()


class Actor(models.Model):
    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    birth_year = models.IntegerField(db_column='birth_year', null=False)

    movies = models.ManyToManyField('Movie', through='MovieActor')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'actors'


class MovieActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    salary = models.IntegerField()
    main_role = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f"{self.actor.name} in movie {self.movie.name}"

    class Meta:
        db_table = 'movie_actors'


# Create your models here.
class Movie(models.Model):

    # https://docs.djangoproject.com/en/4.1/ref/models/options/
    class Meta:
        db_table = 'movies'

    name = models.CharField(null=False, blank=False, db_column='name', db_index=True, max_length=128)
    year = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    # poster_url = models.CharField(null=True, blank=True, max_length=256)
    director = models.ForeignKey(to=Director, on_delete=RESTRICT, null=True, blank=True,
                                 related_name='director_movies')

    actors = models.ManyToManyField(Actor, through='MovieActor')


    def __str__(self):
        return f"{self.name}"




