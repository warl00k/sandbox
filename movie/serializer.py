from rest_framework import serializers
from movie.models import Movie
from person.models import Person
from person.serializer import PersonSerializer


class MovieSerializer(serializers.ModelSerializer):
    actors = PersonSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors']

    def create(self, validated_data):
        actors_data: dict = validated_data.pop('actors')
        movie = Movie.objects.create(**validated_data)
        for actor in actors_data:
            new_actor = Person.objects.create(**actor)
            movie.actors.add(new_actor)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Update the actors field
        actors_data = validated_data.get('actors', [])

        # Clear existing actors
        instance.actors.clear()

        for actor_data in actors_data:
            actor_instance = Person.objects.create(**actor_data)
            instance.actors.add(actor_instance)

        return instance
