from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainSerializer


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer