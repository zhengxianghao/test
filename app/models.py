import random

from django.db import models

# Create your models here.
class Person(models.Model):
    p_name = models.CharField(max_length=20)
    p_age = models.IntegerField(default=18)

class IDCard(models.Model):
    cardNumber = models.IntegerField(default=000000)
    sex = models.BooleanField(default=True)

    id_person = models.OneToOneField(Person)#,on_delete=models.PROTECT

class Hobby(models.Model):
    h_name = models.CharField(max_length=20)
    h_price = models.IntegerField(default=100)

    h_person = models.ForeignKey(Person)