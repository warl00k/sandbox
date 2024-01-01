from rest_framework import serializers
from movie.models import Movie, AssignmentRole
from person.models import Person
from person.serializer import PersonSerializer


class MovieSerializer(serializers.ModelSerializer):
    actors = PersonSerializer(many=True, allow_null=True)
    actors_input = serializers.ListField(
        child=serializers.DictField(), required=False
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors', 'actors_input']

    def create(self, validated_data):
        actors_data = validated_data.pop('actors', [])
        actors_input = validated_data.pop('actors_input', [])

        movie = Movie.objects.create(**validated_data)

        for actor_data in actors_data:
            role_name = actor_data.pop('role', '')
            actor_serializer = PersonSerializer(data=actor_data)

            if actor_serializer.is_valid():
                new_actor = actor_serializer.save()

                AssignmentRole.objects.create(movie=movie, person=new_actor, name=role_name)

        for actor_input in actors_input:
            role_name = actor_input.get('role', '')
            actor_id = actor_input.get('actor_id', None)

            if actor_id is not None:
                try:
                    existing_actor = Person.objects.get(id=actor_id)

                    AssignmentRole.objects.create(movie=movie, person=existing_actor, name=role_name)
                except Person.DoesNotExist:
                    pass

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        actors_data = validated_data.pop('actors_input', [])

        instance.actors.clear()

        for actor_data in actors_data:
            instance.actors.add(actor_data)

        return instance
