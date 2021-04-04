class MoviesDataMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from sw_movies.models import Character, Film
        request.films = Film.objects.all()
        request.characters = Character.objects.all()

        response = self.get_response(request)

        return response
