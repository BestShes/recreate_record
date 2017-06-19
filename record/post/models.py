from django.db import models

from diary.models import Diary


class Post(models.Model):
    diary = models.ForeignKey(Diary)
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Photo(models.Model):
    post = models.ForeignKey(Post)
    photo = models.ImageField()
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
