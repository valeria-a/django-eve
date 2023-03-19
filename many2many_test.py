import os
import django


os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()


from movies_app.models import *

# m = Movie.objects.get(id=3)
# new_actor = Actor(name='ttttt', birth_year=2000)
# new_actor.save()
# ma = MovieActor(movie=m, actor=new_actor, salary=100000, main_role=False)
# ma.save()
# new_actor = Actor.objects.create(name='ppppp', birth_year=1988)
# ma = MovieActor(movie_id=m.id, actor_id=new_actor.id, salary=100000, main_role=False)
# ma.save()
# m.actors.create(name='yyyyyy', birth_year=2001, through_defaults={'salary': 20000000,
#                                                                   'main_role': True})

# m = Movie.objects.get(id=1)
# m.actors.add(Actor.objects.get(id=3), through_defaults={'salary': 2500000,
#                                                         'main_role': False})


# m = Movie.objects.get(id=3)
# a = Actor.objects.get(name__contains='ppp')
# m.actors.remove(a)

# a.delete()

# m = Movie.objects.get(name__iexact='titanic')
# print(m.actor_set.all())
# print(m.movieactor_set.all()[0].actor)
# # print(m.actors_set.all())
# print(m.movieactor_set.all()[0].movie)

#
# a = Actor.objects.get(id=1)
# print(a.movie_set.all())


#
# a = Actor.objects.get(id=3)
# a.movie_set.add(Movie(name='bbbb', year=1999))

# create new actor for movie
titanic_movie = Movie.objects.get(name__iexact='titanic')
# will not work - need to add movieActor fields
# titanic_movie.actors.create(
#     name='Kate Winslet', birth_year=1975)

# titanic_movie.actors.create(
#     name='Bill Paxton', birth_year=1972,
#     through_defaults={'salary': 5000000, 'main_role': True}
# )

# Add existing actor for movie
billy = Actor.objects.get(name__icontains='billy')
# will not work
# titanic_movie.actors.add(billy)

# will work
# titanic_movie.actors.add(
#     billy,
#     through_defaults={'salary': 270000, 'main_role': False})


# Remove actor from the movie
# titanic_movie.actors.remove(billy)

# titanic_movie.actors.clear()
