from django.shortcuts import render, redirect,HttpResponse
from .models import *
import operator
import random
from operator import itemgetter

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        html = "<html><body>You search: %s</body></html>" %search
        if search:
            mylist = makeList(search)
            context = {
                'mylist': mylist,
            }
            return render(request,'search/search_products.html',context)
        else:
            return HttpResponse("BLANK")
    return render(request,'search/search_bar.html')

def makeList(search):
    name = []
    price = []
    link = []
    img = []
    objectList = []

    objectList.append(Web1())
    #objectList.append(Web1())

    for o in objectList:
        o.addSearch(search)
        n, p, l, i = o.fetch()
        name = name + n
        price = price + p
        link = link + l
        img = img + i

    price = list(map(int, price))
    zipped = zip(name, price, link, img)
    mylist = list(zipped)
    return mylist

