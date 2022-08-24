from rest_framework import serializers

#models
from .models import NewsFeeds
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		# fields = '__all__'
		fields = ('username','email','password')


class NewsFeedsSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = NewsFeeds
		fields = '__all__'

'''
{
    "password": "",
    "last_login": null,
    "is_superuser": false,
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": false,
    "is_active": false,
    "date_joined": null,
    "groups": [],
    "user_permissions": []
}
'''
