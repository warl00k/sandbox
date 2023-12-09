from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    publish_date = models.DateField(blank=True, null=True)


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)