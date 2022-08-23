from django.db import models


# Create your models here.
class Photo(models.Model):
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	name = models.CharField(max_length=200, null=True)
	photo = models.ImageField(default="profile1.png",null=True, upload_to='thumbnail')

	def __str__(self):
		return self.name
