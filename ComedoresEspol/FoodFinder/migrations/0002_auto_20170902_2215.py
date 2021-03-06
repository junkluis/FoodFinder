# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFinder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='usuario',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='FoodFinder.Usuario'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodFinder.Usuario'),
        ),
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
