# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFinder', '0003_auto_20170902_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='comedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FoodFinder.Comedor'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='facultad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FoodFinder.Facultad'),
        ),
    ]