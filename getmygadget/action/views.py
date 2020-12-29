from django.db import models
from abc import ABC,abstractmethod
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from django.shortcuts import render, redirect
from .models import Web1



def trend(request):

    name = []
    price = []
    link = []
    img = []

    web = Web1()
    products = web.fetch()



    for p in products:

        name.append( p.find('span', {'class': 'deal-title-container'}).text)
        price.append( p.find('span', {'class': 'deal-price-container'}).text)
        img.append(p.find('img', {'class': 'deal_image'}).get('src'))
        link.append( p.find('a').get('href'))

    mylist = zip(name,price,link,img)
    context = {
        'mylist': mylist,
    }

    return render(request,'action/trend.html',context)
