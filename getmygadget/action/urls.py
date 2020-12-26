from django.urls import path

from . import views

urlpatterns = [
    path('trend', views.trend, name='trend.html'),
    ]