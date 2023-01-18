from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('dht/list', views.getList),
    path('dht/last',views.getLast)
    path('dht/add',views.addData)
]