from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from DtcModels.models import Photo
from .serializer import PhotoSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
	item = Photo.objects.all()
	serializer = PhotoSerializer(item, many=True)
	return Response(serializer.data) 

@api_view(['POST'])
def addItem(request):
	serializer = PhotoSerializer(data =request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
	