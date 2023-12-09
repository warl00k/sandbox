from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MoviesView(APIView):
    def get(self, request):
        # GET /movies/movies
        # List all movies

        movies = Movie.objects.order_by('-name').all()

        serializer = MovieSerializer(data=movies, many=True)
        # serializer.is_valid()

        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        # POST /movies/movies
        # Create new movie

        data: dict = request.data

        movie = Movie(name=data['name'], publish_date=data['publish_date'])
        movie.save()

        return HttpResponse("OK", 200)


class MovieDetailView(APIView):
    def get(self, request, id):
        # GET /movies/movies/{id}
        # Get movie details

        movie = Movie.objects.get(id=id)

        serializer = MovieSerializer(data=movie.__dict__)
        serializer.is_valid()
        return JsonResponse(serializer.data, safe=False)

    def patch(self, request, id):
        # PATCH /movies/movies/{id}
        # Update movie details

        movie = Movie.objects.get(id=id)

        movie.name = request.data['name']
        movie.publish_date = request.data['publish_date']

        movie.save()

        serializer = MovieSerializer(movie.__dict__)
        serializer.is_valid()

        return JsonResponse(serializer.data, safe=False)

    def delete(self, request, id):
        # DELETE /movies/movies/{id}
        # Delete a movie

        try:
            movie = Movie.objects.get(id=id)
            movie.delete()
        except Movie.DoesNotExist:
            return HttpResponse("Not Found", 404)

        return JsonResponse({"status": "success"})
