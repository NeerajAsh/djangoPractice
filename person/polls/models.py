from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=200)
    birthYear=models.IntegerField()
    deathYear=models.IntegerField()
    age = models.IntegerField(default=0)