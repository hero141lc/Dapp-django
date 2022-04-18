from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connectus', views.connectUs, name='connectUs'),
    path('result', views.result, name='result'),
    path('create', views.create, name='create'),
]