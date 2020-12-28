from django.shortcuts import render, redirect
from .models import *
import operator
import random

def trend(request):
    name = []
    price = []
    link = []
    img = []
    objectList = []
    objectList.append(Web1())
    objectList.append(Web2())

    for o in objectList:
        n, p, l, i = o.fetch()
        name = name + n
        price = price + p
        link = link + l
        img = img + i

    zipped = zip(name, price, link, img)
    mylist = list(zipped)
    random.shuffle(mylist)
    context = {
        'mylist': mylist,
    }

    return render(request,'trend/trend.html',context)
