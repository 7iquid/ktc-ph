from django.db import models
from django.contrib.auth.models import User
from django_dropbox_storage.storage import DropboxStorage


DROPBOX_STORAGE = DropboxStorage()


class UserThumbNail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    say = models.CharField(null = True, max_length=250 )
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos', storage=DROPBOX_STORAGE)
    def serialize(self):
        return {
            "user": self.user.username,
            "say": self.say,
            "date": self.date.strftime("%a-%d-%b-%Y , %H:%M:%S %p"),
            "photo": self.photo.url
        }