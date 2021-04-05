from django.shortcuts import render
from sw_movies.forms import FilmSearchForm
from sw_movies.models import Film


def home(request):
    return render(request, "home.html", {})


def search(request):
    context = {}
    if request.method == "POST":
        data = request.POST
        form = FilmSearchForm(data)
        if form.is_valid():
            title_search = data.get("title")
            movies = Film.objects.filter(title__contains=title_search)
            context["movies"] = movies
            context["search_text"] = title_search

    return render(request, "search.html", context)
