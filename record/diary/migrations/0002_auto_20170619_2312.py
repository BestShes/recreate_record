# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='cover_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
