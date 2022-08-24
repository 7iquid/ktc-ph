
class DtcAccount(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.OneToOneField(Photo, on_delete=models.CASCADE, blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True, blank=True)
   	_id = models.AutoField(null=False, primary_key= True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	photo = models.FileField( upload_to='photos', null = True)
	name = models.CharField(max_length=200, null=True)
	photo = models.ImageField(default="profile1.png",null=True, upload_to='thumbnail')

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name