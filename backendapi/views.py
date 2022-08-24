from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import routers, serializers, viewsets

#serializer
from .serializer import  UsersSerializer, NewsFeedsSerializer

#model
from .models import NewsFeeds
from django.contrib.auth.models import User





@api_view(['GET','POST'])
def NewsFeedsView(request):
	item = NewsFeeds.objects.all()
	serializer = NewsFeedsSerializer(item, many=True)
	return Response(serializer.data) 




class NewsFeedsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    serializer_class = NewsFeedsSerializer
    queryset = NewsFeeds.objects.all()
   



# class NewsFeedsViewSet(viewsets.ModelViewSet):
#     serializer_class = NewsFeedsSerializer
#     queryset = NewsFeeds.objects.all()    


# class UsersViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UsersSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UsersSerializer(user)
#         return Response(serializer.data)