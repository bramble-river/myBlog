# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='author',
            field=models.CharField(default='', editable=False, max_length=100),
        ),
    ]