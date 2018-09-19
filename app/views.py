import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Person, IDCard, Hobby


def savePerson(request):
    person = Person.objects.create()
    person.p_name = "小黄人"+str(random.randint(1,100))
    person.p_age = random.randint(1,100)

    person.save()

    return HttpResponse("保存人成功")

def saveIDCard(request):
    person = Person.objects.last()
    idcard = IDCard()
    idcard.cardNumber = random.randint(100000,999999)
    idcard.id_person = person
    idcard.save()

    print("yy")

    return HttpResponse('保存身份证成功')

def delPerson(request):
    person = Person.objects.last()
    # person = Person()
    person.delete()

    return HttpResponse("删除了 人person")

def delIdCard(request):
    idcard = IDCard.objects.last()
    # idcard = IDCard()
    idcard.delete()
    return HttpResponse("删除了 身份证 idcard")

def saveHobby(request):
    person = Person.objects.last()
    hobby = Hobby()
    hobby.h_name = "coding"+str(random.randint(1,100))
    hobby.h_person = person

    hobby.save()
    return  HttpResponse("添加一个爱好")

def getPersonFromCard(request):
    idcard = IDCard.objects.first()
    # idcard = IDCard()
    person = idcard.id_person
    return  HttpResponse("查找一个人"+person.p_name)

def getCardFromProson(request):
    person = Person.objects.last()
    # person = Person()
    idCard = person.idcard
    return HttpResponse("查找一张卡"+str(idCard.cardNumber))

def getPersonFromHobby(request):
    hobby = Hobby.objects.last()
    # hobby = Hobby()
    person = hobby.h_person
    return HttpResponse("查找一个人"+person.p_name)

def getHobbyFromPerson(request):
    person = Person.objects.last()
    person = Person()
    hobbySet = person.hobby_set.all()
    for hobby in hobbySet:
        print(hobby.h_name)

    return HttpResponse("查找多个爱好")