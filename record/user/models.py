from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=MyUserManager.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password):
        u = self.create_user(email=username,
                             nickname=nickname,
                             password=password,
                             )
        u.is_admin = True
        u.is_staff = True
        u.save(using=self._db)
        return u


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

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']
    objects = MyUserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
