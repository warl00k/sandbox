from django.db import models
from person.models import Person
from account.models import Account

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Person, through='AssignmentRole')


class AssignmentRole(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    context = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
