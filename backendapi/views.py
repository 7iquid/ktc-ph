from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import routers, serializers, viewsets

#serializer
from .serializer import  UsersSerializer, NewsFeedsSerializer

#model
from .models import NewsFeeds
from django.contrib.auth.models import User





@api_view(['GET'])
def NewsFeedsView(request):
	item = NewsFeeds.objects.all()
	serializer = NewsFeedsSerializer(item, many=True)
	return Response(serializer.data) 




# class NewsFeedsViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     A simple ViewSet for viewing accounts.
#     """
#     serializer_class = NewsFeedsSerializer
#     queryset = NewsFeeds.objects.all()
   



