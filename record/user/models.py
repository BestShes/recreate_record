from django.db import models


class User(models.Model):
    USER_TYPE = (
        ('normal', 'Normal'),
        ('google', 'Google'),
    )
    username = models.EmailField()
    password = models.CharField(max_length=20, null=True)
    nickname = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100, null=True)
    user_type = models.CharField(max_length=6, choices=USER_TYPE, default='normal')