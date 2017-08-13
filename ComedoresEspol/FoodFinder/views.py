# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import date
from FoodFinder.models import *
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Denuncia
from .serializers import DenunciaSerializer
from django.http import Http404

def index(request):
    template = loader.get_template('FoodFinder/index.html')
    platillos = Platillo.objects.all()
    context = {
        'platillos':platillos,
    }
    return HttpResponse(template.render(context, request))

def galeria(request):
    template = loader.get_template('FoodFinder/photoGallery.html')
    platillos=Platillo.objects.all()
    context = {
        'platillos':platillos,
    }
    return HttpResponse(template.render(context, request))

def comedoresC(request):
    template = loader.get_template('FoodFinder/comedores-cercanos.html')
    comedores = Comedor.objects.all()
    context = {
        'comedores':comedores,
    }
    return HttpResponse(template.render(context, request))

def comedoresF(request):
    template = loader.get_template('FoodFinder/comedoresFacultad.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mejoresPlatos(request):
    template = loader.get_template('FoodFinder/mejores-platos.html')
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('FoodFinder/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def historia(request):
    template = loader.get_template('FoodFinder/time.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contacto (request):
    template=loader.get_template('FoodFinder/contacto.html')
    context={}
    return  HttpResponse(template.render(context, request))


def loginUser(request):
    template = loader.get_template('FoodFinder/login-comd.html')

    if(request.method == 'POST'):
        nombre = request.POST['usuario']
        clave = request.POST['password']
        user = authenticate(username=nombre, password=clave)
        if user is not None:
            usuario = Usuario.objects.get(nombre=nombre);
            if usuario is not None:
                login(request, user)
                if usuario.tipo == "moderador":
                    return redirect('FoodFinder:moderador')
        else:
            notice='Ingreso Invalido'
    else:
        notice='none'
    context = {
        'notice':notice
    }
    return HttpResponse(template.render(context, request))


def ajaxMejoresPlatos(request):
    #username = request.GET.get('username', None)
    mejoresPlatos = Platillo.objects.all().order_by('-valoracion')[:5]
    platillos = []
    for plato in mejoresPlatos:
        platillo = {}
        platillo["nombre"] = plato.titulo
        platillo["valoracion"] = plato.valoracion
        platillos.append(platillo)
    data = {
        #'is_taken': User.objects.filter(username__iexact=username).exists()
        'platillos':platillos
    }
    return JsonResponse(data)


    ajaxValorar

def ajaxValorar(request):
    idPlato = request.GET.get("plato_id")
    puntaje = request.GET.get("valor")
    plato = Platillo.objects.get(pk=idPlato)
    total = plato.valoracion + int(puntaje)

    Platillo.objects.filter(pk=idPlato).update(valoracion=total)

    #username = request.GET.get('username', None)
    data = {
        #'is_taken': User.objects.filter(username__iexact=username).exists()
        'platillos':idPlato
    }
    return JsonResponse(data)

def valoracion(request):
    template=loader.get_template('FoodFinder/valoracion.html')
    platillos = Platillo.objects.all()
    platillosDic={}
    for platillo in platillos:
        platillosDic[platillo.comedor.nombre]=platillosDic.get(platillo.comedor.nombre,[])+[platillo]
    context={"platillosDic": platillosDic}
    return  HttpResponse(template.render(context, request))

def denuncia(request):
    template = loader.get_template('FoodFinder/denuncia.html')
    comedores = Comedor.objects.all()
    context = {
        'comedores':comedores,
        'action': 'Enviar'
    }
    return HttpResponse(template.render(context, request))

def guardarDenuncia(request):
    den = Denuncia()
    den.comedor = request.POST.get('comedor')
    den.fecha_den = request.POST.get('fecha_den')
    den.denuncia = request.POST.get('denuncia')

    den.save()
    return redirect('/FoodFinder/denuncia/')

def sesionModerador(request):
    template = loader.get_template('FoodFinder/sesion-moderador.html')
    usuario = Usuario.objects.get(nombre=request.user.username);
    denuncias = Denuncia.objects.all()
    if usuario is not None:
        usuarioValido = usuario

    context = {
        'usuario': usuarioValido,
        'denuncias': denuncias,
    }
    return HttpResponse(template.render(context, request))

def contacto (request):
    template=loader.get_template('FoodFinder/contacto.html')
    email_host=settings.EMAIL_HOST_USER

    if(request.method== 'POST'):
        nombres_contacto=  request.POST.get('name')
        correo_contacto=   request.POST.get('email')
        asunto_contacto=   request.POST.get('subject')
        mensaje_contacto=  request.POST.get('message')
        email_envio=[email_host,correo_contacto]
        send_mail(asunto_contacto, mensaje_contacto, email_host ,email_envio, fail_silently=True)
    
    else:
        notice='none'
    context = {
        'notice':notice
    }
    return HttpResponse(template.render(context, request))


def platilloInfo(request, pId):
    template=loader.get_template('FoodFinder/platillo.html')
    context = {}
    platillo=Platillo.objects.get(id=pId)
    comedor=platillo.comedor
    context["nombreComedor"]=comedor.nombre
    context["titulo"]=platillo.titulo
    context["precio"]=platillo.precio
    context["horaIni"]=comedor.hora_ini
    context["horaFin"]=comedor.hora_fin
    context["imagen"]=platillo.imagen
    context["tipo"]=platillo.tipo
    context["cantidad"]=platillo.cantidad

    return  HttpResponse(template.render(context, request))

class DenunciaList(APIView):

    def get(self, request):
        stocks = Denuncia.objects.all()
        serializer = DenunciaSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DenunciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DenunciaDetail(APIView):
    def get_object(self, pk):
        try:
            return Denuncia.objects.get(pk=pk)
        except Denuncia.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = DenunciaSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = DenunciaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)