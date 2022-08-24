from django.urls import path, include
from .views import  NewsFeedsView ,NewsFeedsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('NewsFeeds', viewset=NewsFeedsViewSet)

urlpatterns = [
	path('', NewsFeedsView),
	path('router', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

