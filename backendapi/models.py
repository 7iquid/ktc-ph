from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NewsFeeds(models.Model):
	_id = models.AutoField(null=False, primary_key= True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=200, null=False )
	photo = models.ImageField(null=False, upload_to='newsfeeds')

	def __str__(self):
		return self.user