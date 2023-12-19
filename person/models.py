from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
