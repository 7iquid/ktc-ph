# from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# from db_file_storage.compat import url, reverse_lazy
# from django.utils.translation import gettext_lazy as
# from db_file_storage import views as db_file_storage_views

app_name = "main"   

urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)