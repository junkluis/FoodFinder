# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFinder', '0007_auto_20170811_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(default='cliente', max_length=15),
        ),
    ]