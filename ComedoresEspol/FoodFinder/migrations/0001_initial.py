# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=300)),
                ('hora_ini', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('ayudantes', models.BooleanField()),
                ('ubicacion', models.FloatField()),
                ('especialidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('logo', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('distancia', models.FloatField()),
                ('valorNutricional', models.FloatField()),
                ('imagen', models.CharField(max_length=300)),
                ('valoracion', models.IntegerField()),
                ('comedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodFinder.Comedor')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=15)),
                ('comedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodFinder.Comedor')),
            ],
        ),
        migrations.AddField(
            model_name='comedor',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodFinder.Facultad'),
        ),
    ]