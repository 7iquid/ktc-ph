from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
# Create your views here.

@api_view(['GET'])
def getData(request, location='manila'):
	person={'name':'Denis','age':26}
	url = 'http://api.weatherapi.com/v1/current.json'
	key = '8daf2b94b0ef4115bde152002222506'
	params ={
		'key': key,
		'q' : location,
		}
	response = requests.get(url, params=params)

	return Response(response.json())
