from django.urls import path, include
from .views import  getData ,NewsFeedsViewSet
from django.contrib.auth.models import User
from rest_framework import routers


router = routers.DefaultRouter()
router.register('NewsFeeds', viewset=NewsFeedsViewSet)

urlpatterns = [
	path('', getData),
	path('router', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

