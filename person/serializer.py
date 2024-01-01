from rest_framework import serializers
from person.models import Person


class PersonSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Person
        fields = '__all__'
