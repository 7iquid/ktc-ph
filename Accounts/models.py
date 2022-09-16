from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# User = get_user_model()


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='profilePick',null=False, default='profilePick/empty.png')

    def __str__(self):
        return self.username

# class DtcAccount(models.Model):
#     # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     phone = models.CharField(max_length=200, null=True, blank=True)
#     email = models.CharField(max_length=200, null=True, blank=True)
#     date_created = models.DateTimeField(auto_now_add=True ,null=True, blank=True)

#     def __str__(self):
#         return self.name
# class DtcAccount(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(,)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     say = models.CharField(null = True, max_length=250 )
#     # photo = models.ImageField( null=True, upload_to='photo' )
#     # image = models.FileField()
#     # image_data = models.BinaryField(null=True)
#     # player_photo = models.ImageField(upload_to="player_photos", storage=DatabaseStorage() )
#     photo = models.ImageField( )

# class ImageFile(models.Model):
#     image = models.FileField()
#     image_data = models.BinaryField(null=True)
    # print(download())

# print(list_folder(dbx, '/DTC', 'newsfeeds')) 