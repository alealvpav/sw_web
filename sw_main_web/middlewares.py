class MoviesDataMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from sw_movies.models import Character, Film
        request.films = Film.objects.all()
        request.characters = Character.objects.all()

        response = self.get_response(request)

        return response


class SearchFormMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from sw_movies.forms import FilmSearchForm
        request.search_form = FilmSearchForm()

        response = self.get_response(request)

        return response


class PagesHistoryMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            previous_url = request.META.get('HTTP_REFERER')
            if previous_url:
                request.session.get('history').append(previous_url)
        except Exception:
            request.session['history'] = []

        response = self.get_response(request)

        return response
