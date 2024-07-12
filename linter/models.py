from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField()
    color = models.CharField(max_length=100)
    is_new = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
