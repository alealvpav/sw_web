from django.urls import path
from . import views

urlpatterns = [
    path("movie/<int:movie_pk>", views.movie_detail, name="movie"),
    path("character/<int:character_pk>", views.character_detail, name="character"),
]
