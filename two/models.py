from django.db import models

# Create your models here.
class Buyer(models.Model):
    b_name = models.CharField(max_length=20)
    b_age = models.IntegerField(default=18)

class Goods(models.Model):
    g_name = models.CharField(max_length=20)
    g_price = models.IntegerField(default=100)

    g_buyer = models.ManyToManyField(Buyer)

