from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from movie.serializer import MovieSerializer
from movie.models import Movie
import json
from person.models import Person


class MovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        # actors_data_str = data.get('actors', '[]')
        # actors_data = json.loads(actors_data_str)
        # persons = Person.objects.filter(id__in=actors_data)
        data = request.data
        movie = Movie(title=data.get('title'), description=data.get('description'))
        movie.save()
        actors = data.get('actors')
        for _ in actors:
            movie.actors.add(_)
        return HttpResponse('Movie created', status=201)
        # if serializer.is_valid():
        #
        #
        # return JsonResponse(serializer.errors, status=400)


class MovieDetailView(APIView):
    def get(self, request, id):
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return HttpResponse('Movie not found', status=404)

        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, safe=False)

    def patch(self, request, id):
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return JsonResponse('Movie not found', status=404)

        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id):
        try:
            movie = Movie.objects.get(id=id)
            movie.delete()
            return JsonResponse('Movie deleted', safe=False, status=204)
        except Movie.DoesNotExist:
            return JsonResponse('Movie not found', safe=False, status=404)


