from django.db import models

from user.models import Member


class Diary(models.Model):
    author = models.ForeignKey(Member)
    title = models.CharField(max_length=50)
    cover_img = models.ImageField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
