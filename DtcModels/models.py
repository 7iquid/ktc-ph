from django.db import models


# Create your models here.


# class NewsFeeds(models.Model):
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	category = models.CharField(max_length=200, null=True)
# 	# photo =models.ForeignKey(Photo, on_delete=models.CASCADE,null=True)

# 	def __str__(self):
# 		return self.category


# class Photo(models.Model):
# 	name = models.CharField(max_length=200, null=False)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	photo = models.ImageField(default="profile1.png",null=True, upload_to='thumbnail')
# 	news =models.ForeignKey(NewsFeeds, on_delete=models.CASCADE,null=True)
	
# 	def __str__(self):
# 		return self.date_created