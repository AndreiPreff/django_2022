from . import views
from django.urls import path
from .views import ListDirectors, ListActors



urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', ListDirectors.as_view(), name='all_directors'),
    path('director/<int:id_director>', views.show_one_director, name='one_director'),
    path('actors/', ListActors.as_view(), name='all_actors'),
    path('actor/<int:id_actor>', views.show_one_actor, name='one_actor'),
]

# path('directors/', views.show_all_directors, name='all_directors'),
# path('actors/', views.show_all_actors, name='all_actors'),