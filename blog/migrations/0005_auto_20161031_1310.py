# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161031_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
