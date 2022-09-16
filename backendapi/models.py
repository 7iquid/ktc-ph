from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class NewsFeeds(models.Model):
	_id = models.AutoField(null=False, primary_key= True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=200, null=False,default=None )
	photo = models.ImageField(null=False, upload_to='newsfeeds', default=None)

	def __int__(self):
		return self.user