# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFinder', '0002_auto_20170902_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='aceptado',
            field=models.IntegerField(default=0),
        ),
    ]