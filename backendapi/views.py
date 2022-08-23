from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import routers, serializers, viewsets

#serializer
from .serializer import PhotoSerializer, UsersSerializer, NewsFeedsSerializer

#model
from DtcModels.models import Photo,NewsFeeds
from django.contrib.auth.models import User


@api_view(['GET','POST'])
def getData(request):
	item = Photo.objects.all()
	serializer = PhotoSerializer(item, many=True)
	return Response(serializer.data) 


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

class NewsFeedsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsFeedsSerializer
    queryset = NewsFeeds.objects.all()    