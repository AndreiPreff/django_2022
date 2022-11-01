from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.views.generic import ListView

# Create your views here.
from .models import Movie, Director, Actor

def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True))
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('Hello'),
        int_field=Value(123),
        new_budget=F('budget')+100)
    agg = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'))

    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


class ListDirectors(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'

class ListActors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'



# def show_all_directors(request):
#     directors = Director.objects.order_by(F('first_name'))
#     return render(request, 'movie_app/all_directors.html', {
#         'directors': directors,
#         'total': directors.count()
#     })


def show_one_director(request, id_director: int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })

# def show_all_actors(request):
#     actors = Actor.objects.order_by(F('first_name'))
#     return render(request, 'movie_app/all_actors.html', {
#         'actors': actors,
#         'total': actors.count()
#     })


def show_one_actor(request, id_actor: int):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor
    })

