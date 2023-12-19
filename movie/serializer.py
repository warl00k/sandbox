from rest_framework import serializers
from movie.models import Movie
from person.serializer import PersonSerializer


class MovieSerializer(serializers.ModelSerializer):
    actors = PersonSerializer(many=True)

    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'actors']
