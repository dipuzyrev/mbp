from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from main.models import *


User = get_user_model()

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': {
            'detail': [u'Неверный логин или пароль. Пожалуйста, попробуйте еще раз.']
        }
    }

    # @classmethod
    # def get_token(cls, user):
    #     return super().get_token(user)