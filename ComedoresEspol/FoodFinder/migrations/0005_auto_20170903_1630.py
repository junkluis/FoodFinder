# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFinder', '0004_remove_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombreUsu',
            field=models.CharField(default='carlitos', max_length=30, unique=True),
        ),
    ]