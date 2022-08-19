from django.db import models
from django.contrib.auth.models import User
# from django.core.files.storage import FileSystemStorage
# from django.conf.urls.static import static
# from django.conf import settings
# from django_dropbox_storage.storage import DropboxStorage
# from backendapi.updown import download , list_folder
# import dropbox
# DROPBOX_STORAGE = DropboxStorage()
# TOKEN = settings.DROPBOX_OAUTH2_TOKEN
# dbx = dropbox.Dropbox(settings.DROPBOX_OAUTH2_TOKEN)
class UserThumbNail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # say = models.CharField(null = True, max_length=250 )
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo' , null = True,)
    # image = models.FileField()
    # image_data = models.BinaryField(null=True)
    # player_photo = models.ImageField(upload_to="player_photos", storage=DatabaseStorage() )
    # photo = models.FileField( upload_to='photos',)
# class ImageFile(models.Model):
#     image = models.FileField()
#     image_data = models.BinaryField(null=True)
    # print(download())

# print(list_folder(dbx, '/DTC', 'newsfeeds')) 