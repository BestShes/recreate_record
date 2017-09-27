from django.conf import settings
from django.db import models


class Diary(models.Model):
    TRAVEL_AREA = (
        ('EU', 'Europe'),
        ('NA', 'North America'),
        ('SA', 'South America'),
        ('KR', 'Korea'),
        ('ASIA', 'Asia'),
        ('OCE', 'Oceania'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    cover_img = models.ImageField(blank=True)
    travel_area = models.CharField(choices=TRAVEL_AREA, max_length=17)
    travel_start_date = models.DateField(null=True)
    travel_end_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
