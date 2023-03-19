import datetime
import os
import django
from django.db.models import Q

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()


from movies_app.models import Movie, Director

if __name__ == '__main__':

    # inefficient
    for movie in Movie.objects.all():
        print(movie.name, movie.director.name)

    # for movie in Movie.objects.all().select_related('director'):
    #     print(movie.name, movie.director.name)

    # for movie in Movie.objects.all().prefetch_related('director'):
    #     print(movie.name, movie.director.name)

    # director = Director.objects.get(pk=1)
    # print(director.director_movies.all())

    # directors = Director.objects.all().prefetch_related('director_movies')
    # for d in directors:
    #     print(d.director_movies.all())