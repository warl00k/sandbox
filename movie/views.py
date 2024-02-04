from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from movie.serializer import MovieSerializer, CommentSerializer
from movie.models import Movie
import json
from person.models import Person
from .models import Comment


class MovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = request.data
        serializer = MovieSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Movie created', status=201)
        return JsonResponse(serializer.errors, status=400)


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


class CommentView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = request.data
        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Comment created', status=201)
        return JsonResponse(serializer.errors, status=400)

class CommentDetailView(APIView):
    def get(self, request, id):
        try:
            comment = Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            return HttpResponse('Comment not found', status=404)

        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data, safe=False)

    def patch(self, request, id):
        try:
            comment = Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            return JsonResponse('Comment not found', status=404)

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id):
        try:
            comment = Comment.objects.get(id=id)
            comment.delete()
            return JsonResponse('Comment deleted', safe=False, status=204)
        except Comment.DoesNotExist:
            return JsonResponse('Comment not found', safe=False, status=404)