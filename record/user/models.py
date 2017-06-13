from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    USER_TYPE = (
        ('normal', 'Normal'),
        ('google', 'Google'),
    )
    username = models.EmailField()
    password = models.CharField(max_length=100, null=True)
    nickname = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100, null=True)
    user_type = models.CharField(max_length=6, choices=USER_TYPE, default='normal')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']
