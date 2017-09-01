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
    latitud=models.FloatField(default=0)
    longitud=models.FloatField(default=0)

class Platillo(models.Model):
    comedor=models.ForeignKey(Comedor, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    precio=models.FloatField()
    cantidad=models.IntegerField()
    imagen=models.CharField(max_length=500)
    valoracion=models.IntegerField()

class Usuario(models.Model):
    facultad=models.ForeignKey(Facultad, on_delete=models.CASCADE,default="1")
    nombreUsu=models.CharField(max_length=30,default="carlitos")
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30,default="suarez")
    correo=models.EmailField(max_length=30)
    password=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15, default="cliente")
    ROLES=(
        ('Estudiante', 'Estudiante'),
        ('Docente', 'Docente'),
        ('Trabajador', 'Trabajador'),
    )
    rol=models.CharField(max_length=10, choices=ROLES, default="Estudiante")

class Denuncia(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,default="1")
    comedor=models.CharField(max_length=30)
    fecha_den=models.DateField()
    denuncia=models.CharField(max_length=1000)

class Timeline(models.Model):
    fecha=models.CharField(max_length=30)
    descp=models.CharField(max_length=200)

class Comentario(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comedor=models.ForeignKey(Comedor, on_delete=models.CASCADE)
    #usuario=models.CharField(max_length=30)
    comentario=models.CharField(max_length=1000)
