from rest_framework.serializers import ModelSerializer

from movies.models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'publish_date', 'description']
