import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from two.models import Buyer, Goods


def addBuyer(request):
    buyer = Buyer.objects.create()
    buyer.b_name = "三胖胖"+str(random.randint(1,100))
    buyer.save()
    return HttpResponse("添加了buyer")

def addGoods(request):
    goods = Goods()
    goods.g_name = "娃娃"+str(random.randint(1,100))
    goods.save()
    return HttpResponse("添加了goods")

def addGoodsAndBuyer(request):
    buyer = Buyer.objects.last()
    goods = Goods.objects.last()
    # goods = Goods()
    goods.g_buyer.add(buyer)
    goods.save()
    return HttpResponse("添加了订单")

def delBuyer(request):
    buyer = Buyer.objects.first()
    # buyer = Buyer()
    buyer.delete()
    return HttpResponse("删除了购买者")

def delGoods(request):
    goods = Goods.objects.first()
    # goods = Goods()
    goods.delete()

    return HttpResponse("删除了商品")
