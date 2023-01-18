from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DhtSerializer
from myrestapi.models import Dht

@api_view(['GET'])
def getList(request):
    queryset = Dht.objects.all().order_by('-dt')
    serializer = DhtSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLast(request):
    item = Dht.objects.all().last()
    serializer = DhtSerializer(item)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = DhtSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)