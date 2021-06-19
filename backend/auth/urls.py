from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from .views import *


urlpatterns = [
    path('jwt/create/', CustomTokenObtainView.as_view(), name="jwt-create"),
    path('jwt/refresh/', jwt_views.TokenRefreshView.as_view(), name="jwt-refresh"),
    path('jwt/verify/', jwt_views.TokenVerifyView.as_view(), name="jwt-verify"),
]
