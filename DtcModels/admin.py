from django.contrib import admin

# Register your models here.
from .models import Photo,NewsFeeds

admin.site.register(Photo)
admin.site.register(NewsFeeds)