from django.forms import CharField, ModelForm

from sw_movies.models import Film


class FilmSearchForm(ModelForm):

    class Meta:
        model = Film
        fields = ["title"]
