# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Facultad(models.Model):
    nombre=models.CharField(max_length=30)
    logo=models.CharField(max_length=300)

class Comedor(models.Model):
    facultad=models.ForeignKey(Facultad, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=300)
    hora_ini=models.TimeField()
    hora_fin=models.TimeField()
    ayudantes=models.BooleanField()
    ubicacion=models.FloatField()
    especialidad=models.CharField(max_length=30)

class Platillo(models.Model):
    comedor=models.ForeignKey(Comedor, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    precio=models.FloatField()
    cantidad=models.IntegerField()
    distancia=models.FloatField()
    valorNutricional=models.FloatField()
    imagen=models.CharField(max_length=300)
    valoracion=models.IntegerField()

class Usuario(models.Model):
    comedor=models.ForeignKey(Comedor, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30)
    correo=models.EmailField(max_length=30)
    password=models.CharField(max_length=15)
