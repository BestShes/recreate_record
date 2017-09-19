from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models

class Member(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('normal', 'Normal'),
        ('google', 'Google'),
    )
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=6, choices=USER_TYPE, default='normal')

    USERNAME_FIELD = 'username'
    objects = UserManager()
