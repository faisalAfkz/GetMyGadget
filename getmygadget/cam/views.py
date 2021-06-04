from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
import operator
import random

def index(request):
    context = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    context = {
        'context': context,
    }
    return render(request, 'cam/stream.html',context)
