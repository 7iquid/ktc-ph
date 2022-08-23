# from django.urls import path, include
from .views import register_request, MyTokenObtainPairView
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView,)
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
    path("register", register_request, name="register"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)