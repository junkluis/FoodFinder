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
    comedores = Comedor.objects.all()
    platillos = Platillo.objects.all()
    facultades = Facultad.objects.all()
    context = {
        'comedores': comedores,
        'platillos': platillos,
        'facultades': facultades,
    }
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
    historias=Timeline.objects.all()
    context={
        "historia":historias,
    }

    return  HttpResponse(template.render(context, request))

def contacto (request):
  template=loader.get_template('FoodFinder/contacto.html')
  email_host=settings.EMAIL_HOST_USER

  if(request.method == 'POST'):
        nombres_contacto=  request.POST.get('name')
        correo_contacto=   request.POST.get('email')
        asunto_contacto=   request.POST.get('subject')
        mensaje_contacto=  request.POST.get('message')
        email_envio=[email_host,correo_contacto]
        send_mail(asunto_contacto, mensaje_contacto, email_host ,email_envio, fail_silently=False)
        notice="Gracias por contactarnos, estaremos en contacto!"
        return redirect('FoodFinder/contacto.html')
  else:
        notice='Ingreso no valido'
  context = {
        'notice':notice
  }
  return HttpResponse(template.render(context, request))

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
                if usuario.tipo == "admin":
                    return redirect('FoodFinder:admin')
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
def sesionAdmin(request):
    template = loader.get_template('FoodFinder/sesion-comedor.html')
    usuario = Usuario.objects.get(nombre=request.user.username);
    facultades = Facultad.objects.all()
    usuarios=Usuario.objects.all()
    facUsu={}
    for usu in usuarios:
        fac=usu.comedor.facultad
        facUsu[fac]=facUsu.get(fac,0)+1
    for fac in facultades:
        facUsu[fac]=facUsu.get(fac,0)
    if usuario is not None:
        usuarioValido = usuario
    context = {
        'usuario': usuarioValido,
        'facultades': facUsu,
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

def comedorInfo(request, comId):
    template=loader.get_template('FoodFinder/comedor.html')
    comedor = Comedor.objects.get(id=comId)
    facultad = comedor.facultad
    platillos = platillos.objects.all()
    context["nombre"] = comedor.nombre
    context["tipo"] = comedor.tipo
    context["descripcion"] = comedor.descripcion
    context["hora_ini"] = comedor.hora_ini
    context["hora_fin"] = comedor.hora_fin
    context["ayudantes"] = comedor.ayudantes
    context["facultad"] = facultad.nombre
    context["logo"] = facultad.logo
    context = {
        'platillos':platillos,
    }

    return  HttpResponse(template.render(context, request))
