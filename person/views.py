from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from person.models import Person
from person.serializer import PersonSerializer


class PersonView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Person created', status=201)
        return JsonResponse(serializer.errors, status=400)


class PersonDetailView(APIView):
    def get(self, request, id):
        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return HttpResponse('Person not found', status=404)

        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data, safe=False)

    def patch(self, request, id):
        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return JsonResponse('Person not found', status=404)

        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id):
        try:
            person = Person.objects.get(id=id)
            person.delete()
            return JsonResponse('Person deleted', safe=False, status=204)
        except Person.DoesNotExist:
            return JsonResponse('Person not found', safe=False, status=404)
