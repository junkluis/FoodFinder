# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFinder', '0008_remove_usuario_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
