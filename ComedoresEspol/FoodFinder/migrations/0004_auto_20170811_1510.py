# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFinder', '0003_denuncia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='comedor',
            field=models.CharField(max_length=30),
        ),
    ]
