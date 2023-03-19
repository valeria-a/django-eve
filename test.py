import datetime
import os
import django
from django.db.models import Q

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()


from movies_app.models import Movie, Director

if __name__ == '__main__':
    # Movie(name='titanic', year=1999).save()
    # query_set = Movie.objects.all()
    # print(query_set)
    # qs = Movie.objects.filter(name='Avatar', year=2000)
    # print(qs)
    # (Q(year__gte=1990) | Q(year__gte=1990))
    # qs = Movie.objects.all()
    # print(qs.query)
    # qs = qs.filter(year__gte=1990)
    # print(qs.query)
    # print(qs.count())
    # qs = Movie.objects.filter(year__gte=1990, name__icontains='a')
    # for movie in qs:

    # print(qs)

    # movie = Movie.objects.get(id=1)
    # director = Director.objects.create(
    #     name='James Cameron', birth_date=datetime.date(1954, 8, 16))
    # print(director)
    # print(movie)
    # movie.director = Director.objects.get(id=1)


    # movie = Movie.objects.get(id=3)

    # option 1
    # director = Director.objects.create(name='aaa', birth_date=datetime.date.today())
    # option 2
    # director = Director(name='aaa', birth_date=datetime.date.today())
    # director.save()

    #
    # movie.director = director
    # movie.save()


    # for movie in Movie.objects.all():
    #     print(movie.name, movie.director.name)

    # Movie.objects.get(id=1).delete()
    # Movie.objects.filter(id__in=[1,2,3]).delete()

    # movie = Movie.objects.create(name='avatar', year=2001)
    # movie.director_id = 1
    # movie.save()

    # movie = Movie.objects.create(name='titanic', year=1998)
    # movie.director_id=1
    # movie.save()

    # director = Director.objects.get(pk=1)
    # print(director.movie_set.all())
    # print(director.director_movies.all())

    # Director.objects

    print(Movie.objects.filter(director__name__icontains='p'))