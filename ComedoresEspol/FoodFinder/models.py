# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Facultad(models.Model):
    nombre=models.CharField(max_length=30)
    logo=models.CharField(max_length=300)

    def __str__(self):
        return 'Facultad: {}'.format(self.nombre)

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

    def __str__(self):
        return 'Comedor: {}'.format(self.nombre)

class Platillo(models.Model):
    comedor=models.ForeignKey(Comedor, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    precio=models.FloatField()
    cantidad=models.IntegerField()
    imagen=models.CharField(max_length=500)
    valoracion=models.IntegerField()

    def __str__(self):
        return 'Platillo: {}'.format(self.titulo)

class Usuario(models.Model):
    facultad=models.ForeignKey(Facultad, on_delete=models.CASCADE,blank=True,null=True)
    comedor=models.ForeignKey(Comedor, on_delete=models.CASCADE,blank=True,null=True)
    nombreUsu=models.CharField(max_length=30,default="carlitos", unique=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30,default="suarez")
    correo=models.EmailField(max_length=30)
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

    def __str__(self):
        return 'Denuncia a: {}'.format(self.comedor)

class Timeline(models.Model):
    fecha=models.CharField(max_length=30)
    descp=models.CharField(max_length=200)

    def __str__(self):
        return 'Timeline date: {}'.format(self.fecha)

class Comentario(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comedor=models.ForeignKey(Comedor, on_delete=models.CASCADE)
    comentario=models.CharField(max_length=1000)
    aceptado=models.IntegerField(default=0)

    def __str__(self):
        return 'Comentario: {}'.format(self.comentario)
