# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogspost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='author',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
