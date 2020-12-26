from django.shortcuts import render, redirect
from .models import Web1
import operator
import random

def trend(request):
    name = ['']
    price = ['']
    link = ['']
    img = ['']

    web = Web1()
    name, price, link, img = web.fetch()

    zipped = zip(name,price,link,img)
    mylist = list(zipped)
    random.shuffle(mylist)
    context = {
        'mylist': mylist,
    }

    return render(request,'action/trend.html',context)
