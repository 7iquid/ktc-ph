from rest_framework import serializers

#models
from DtcModels.models import Photo, NewsFeeds
from django.contrib.auth.models import User

class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photo
		fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class NewsFeedsSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsFeeds
		fields = '__all__'

