from django.db import models


# Create your models here.

class Location(models.Model):
	_id = models.AutoField(null=False, primary_key= True)
	street = models.CharField(max_length=40)
	barangay = models.CharField(max_length=40)

	def __str__(self):
		return self._id