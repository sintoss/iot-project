from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DhtSerializer
from .models import Dht

@api_view(['GET'])
def getList(request):
    queryset = Dht.objects.all().order_by('-dt')
    serializer = DhtSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLast(request):
    queryset = Dht.objects.all().order_by('-dt')
    serializer = DhtSerializer(queryset[0], many=True)
    return Response(serializer.data)