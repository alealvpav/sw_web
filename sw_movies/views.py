from django.shortcuts import render, get_object_or_404
from sw_movies.models import Film, Character


def movie_detail(request, movie_pk):
    """
    View to render a SW Movie details page
    :param request: Request object
    :param movie_pk: PK of the movie requested in the URL
    :return: Render SW Movie details (404 if invalid movie_pk)
    """
    sw_movie = get_object_or_404(Film, pk=movie_pk)
    characters = []
    for character in sw_movie.characters.all():
        character_dict = {
            "pk": character.pk,
            "name": character.name,
            "image": character.characterimage_set.first(),
        }
        characters.append(character_dict)

    context = {"movie": sw_movie, "movie_characters": characters}

    return render(request, template_name="sw_movies/movie_detail.html", context=context)


def character_detail(request, character_pk):
    """
    View to render a SW Character details page
    :param request: Request object
    :param character_pk: PK of the Character requested in the URL
    :return: Render SW Character details (404 if invalid character_pk)
    """
    sw_character = get_object_or_404(Character, pk=character_pk)
    movies = sw_character.film_set.all()

    context = {
        "movies": movies,
        "character": sw_character,
    }

    return render(
        request, template_name="sw_movies/character_detail.html", context=context
    )
