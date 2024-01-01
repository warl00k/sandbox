from rest_framework import serializers
from movie.models import Movie, AssignmentRole
from person.models import Person
from person.serializer import PersonSerializer


class MovieSerializer(serializers.ModelSerializer):
    actors_input = serializers.ListField(
        child=serializers.DictField(), required=False
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors', 'actors_input']

    def create(self, validated_data):
        persons_input = validated_data.pop('actors_input', [])

        movie = Movie.objects.create(**validated_data)

        for p in persons_input:
            role_name = p.get('role', '')
            actor_id = p.get('actor_id', None)

            if actor_id is None or role_name is None:
                continue

            AssignmentRole.objects.create(movie=movie, person_id=actor_id, name=role_name)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        persons_data = validated_data.pop('actors_input', [])

        instance.actors.clear()

        for p in persons_data:
            role_name = p.get('role', '')
            actor_id = p.get('actor_id', None)

            if actor_id is None or role_name is None:
                raise Exception()

            AssignmentRole.objects.create(movie=instance, person_id=actor_id, name=role_name)
        return instance
