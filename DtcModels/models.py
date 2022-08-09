from django.db import models

# Create your models here.
class Photo(models.Model):
	_id = models.AutoField(null=False, primary_key= True)
	size = models.IntegerField()
	num_stars = models.IntegerField()
	file = models.BinaryField()


	def __str__(self):
		return self._id