from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from .managers import CustomUserManager


class User(AbstractUser):
    """
    Custom User model, use Email as username

    Default Django User fields, not stated here but existing:
    - password, first_name, last_name, date_joined, last_login
    - is_superuser, is_staff, is_active, user_permissions, groups
    """

    # Email and it's activation status and token
    email = models.EmailField(max_length=320, unique=True)
    USERNAME_FIELD = 'email'

    # Set username as non-required field
    username = models.CharField(max_length=1, blank=True, default='', help_text='Just skip this')

    snils = models.TextField()
    age = models.PositiveIntegerField()
    gender = models.TextField()
    phone = models.TextField()
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    tonometer = models.ForeignKey('Tonometer', on_delete=models.SET_NULL, null=True, blank=True, related_name='patient_tonometer')

    # A list of the field names that will be prompted for when creating a user via the
    # 'createsuperuser' management command
    REQUIRED_FIELDS = ['snils', 'age', 'gender', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'


class Measurement(models.Model):
    """
    Measurements from tonometer
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    upper = models.PositiveIntegerField()
    bottom = models.PositiveIntegerField()
    pulse = models.PositiveIntegerField()
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.upper} / {self.bottom} ({self.pulse}) - {self.user}'


class Treatment(models.Model):
    """
    Treatment notes from doc
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} ({self.date})'


class Notes(models.Model):
    """
    Doc's private notes
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user}'


class Tonometer(models.Model):
    """
    Tonometers
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tonometer_patient')
    name = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.user})'