# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import date
from FoodFinder.models import *
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
    template = loader.get_template('FoodFinder/index.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    platillos = Platillo.objects.all()
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        'platillos':platillos,
    }
    return HttpResponse(template.render(context, request))

def galeria(request):
    template = loader.get_template('FoodFinder/photoGallery.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    platillos=Platillo.objects.all()
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        'platillos':platillos,
    }
    return HttpResponse(template.render(context, request))

def comedoresC(request):
    template = loader.get_template('FoodFinder/comedores-cercanos.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    comedores = Comedor.objects.all()
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        'comedores':comedores,
    }
    return HttpResponse(template.render(context, request))

def comedoresF(request):
    template = loader.get_template('FoodFinder/comedoresFacultad.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    comedores = Comedor.objects.all()
    platillos = Platillo.objects.all()
    facultades = Facultad.objects.all()
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        'comedores': comedores,
        'platillos': platillos,
        'facultades': facultades,
    }
    return HttpResponse(template.render(context, request))

def mejoresPlatos(request):
    template = loader.get_template('FoodFinder/mejores-platos.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('FoodFinder/about.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
    }
    return HttpResponse(template.render(context, request))

def historia(request):
    template = loader.get_template('FoodFinder/time.html')
    historias=Timeline.objects.all()
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        "historia":historias,
    }
    return  HttpResponse(template.render(context, request))

def contacto (request):
    template=loader.get_template('FoodFinder/contacto.html')
    email_host=settings.EMAIL_HOST_USER
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    if(request.method == 'POST'):
        nombres_contacto=  request.POST.get('name')
        correo_contacto=   request.POST.get('email')
        asunto_contacto=   request.POST.get('subject')
        mensaje_contacto=  request.POST.get('message')
        email_envio=[email_host,correo_contacto]
        send_mail(asunto_contacto, mensaje_contacto, email_host ,email_envio, fail_silently=False)
        messages.success(request, 'Gracias por contactarnos!')
    context = {
        'usuario': usuarioValido,
    }
    return HttpResponse(template.render(context, request))

def loginUser(request):
    template = loader.get_template('FoodFinder/login-comd.html')
    if(request.method == 'POST'):
        nombre = request.POST['usuario']
        clave = request.POST['password']
        user = authenticate(username=nombre, password=clave)
        if user is not None:
            usuario = Usuario.objects.get(nombreUsu=nombre);
            if usuario is not None:
                login(request, user)
                if usuario.tipo == "moderador":
                    return redirect('FoodFinder:moderador')
                if usuario.tipo == "admin":
                    return redirect('FoodFinder:admin')
                if usuario.tipo == "cliente":
                    return redirect('FoodFinder:cliente')
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
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        "platillosDic": platillosDic
    }
    return  HttpResponse(template.render(context, request))

def denuncia(request):
    template = loader.get_template('FoodFinder/denuncia.html')
    comedores = Comedor.objects.all()
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        'comedores':comedores,
        'action': 'Enviar'
    }
    return HttpResponse(template.render(context, request))

def guardarDenuncia(request):
    if (request.POST):
        den = Denuncia()
        den.comedor = request.POST.get('comedor')
        den.fecha_den = request.POST.get('fecha_den')
        den.denuncia = request.POST.get('denuncia')

        den.save()
        messages.success(request, 'Su denuncia se envió correctamente!')
    return redirect('/FoodFinder/denuncia/')

def sesionModerador(request):
    template = loader.get_template('FoodFinder/sesion-moderador.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    denuncias = Denuncia.objects.all()

    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    denunciasDic={}
    for den in denuncias:
        denunciasDic[den.comedor]=denunciasDic.get(den.comedor,0)+1

    context = {
        'usuario': usuarioValido,
        'denunciasDic':denunciasDic,
        'denuncias': denuncias
    }

    return HttpResponse(template.render(context, request))

def sesionAdmin(request):
    template = loader.get_template('FoodFinder/sesion-comedor.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
        comedorUsr = usuario.comedor
    except Usuario.DoesNotExist:
        usuario = None
    facultades = Facultad.objects.all()
    usuarios=Usuario.objects.all()
    platillos = Platillo.objects.filter(comedor = comedorUsr)
    facUsu={}
    for usu in usuarios:
        fac=usu.facultad
        facUsu[fac]=facUsu.get(fac,0)+1
    for fac in facultades:
        facUsu[fac]=facUsu.get(fac,0)
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        'facultades': facUsu,
        'comedor': comedorUsr,
        'platillos': platillos,
    }
    return HttpResponse(template.render(context, request))

def actualizarInfoAdmin(request):
    descrip = request.GET.get("descrip")
    especialidad = request.GET.get("especialidad")
    Nombrefac = request.GET.get("facultad")
    ayudantes = request.GET.get("ayudantes")
    horaInicio = request.GET.get("horaInicio")
    horaCierre = request.GET.get("horaCierre")
    comedorPk = int(request.GET.get("comedorPk"))

    facultad = Facultad.objects.get(nombre = Nombrefac)
    comedor = Comedor.objects.get(pk = comedorPk)
    comedor.descripcion = descrip
    comedor.facultad = facultad
    if ayudantes == "false":
        comedor.ayudantes = True
    else:
        comedor.ayudantes = False
    comedor.tipo = especialidad
    comedor.hora_ini = horaInicio
    comedor.hora_fin = horaCierre
    comedor.save()
    data = {
        'descrip':descrip,
        'especialidad':especialidad,
        'Nombrefac':Nombrefac,
        'ayudantes':ayudantes,
        'hora_ini':horaInicio,
        'hora_fin':horaCierre,
    }

    return JsonResponse(data)

def actualizarUbicacion(request):
    newLat = float(request.GET.get("newLat"))
    newLon = float(request.GET.get("newLon"))
    comedorPk = request.GET.get("comedorPk")
    comedor = Comedor.objects.get(pk = comedorPk)
    comedor.latitud = newLat
    comedor.longitud = newLon
    comedor.save()
    data = {
        'descrip':'todo bien',
    }
    return JsonResponse(data)

def MenuDelDiaAdmin(request):
    data = {
        'descrip':'todo bien',
    }
    return JsonResponse(data)

def estadisticasAdmin(request):
    data = {
        'descrip':'todo bien',
    }
    return JsonResponse(data)



def sesionCliente(request):
    template = loader.get_template('FoodFinder/sesion-cliente.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    facultades = Facultad.objects.all()
    context = {
        'usuario': usuarioValido,
        'facultades': facultades
    }
    return HttpResponse(template.render(context, request))

def platilloInfo(request, pId):
    template=loader.get_template('FoodFinder/platillo.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido
    }
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
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    comedor = Comedor.objects.get(id=comId)
    facultad = comedor.facultad
    platillos = Platillo.objects.all()
    comentarios = Comentario.objects.all()
    context = {
        'usuario': usuarioValido,
        'platillos':platillos,
        'comentarios':comentarios,
        'nombre':comedor.nombre,
        'tipo':comedor.tipo,
        'descripcion':comedor.descripcion,
        'hora_ini':comedor.hora_ini,
        'hora_fin':comedor.hora_fin,
        'ayudantes':comedor.ayudantes,
        'facultad':facultad.nombre,
        'logo':facultad.logo,
        'comId':comId,
    }

    return  HttpResponse(template.render(context, request))

def guardarComentario(request):
    if (request.POST):
        comen = Comentario()
        comId = request.POST.get('comId')
        comen.comedor = Comedor.objects.get(id=comId)
        #comen.usuario = Usuario.objects.get(id=request.user.id);
        comen.usuario = Usuario.objects.get(id=request.POST.get('usuarioId'));
        #comen.usuario = request.POST.get('usuario')
        comen.comentario = request.POST.get('comentario')
        comen.aceptado=0
        comen.save()
        messages.success(request, 'Su comentario se guardó correctamente!')
    return redirect('/FoodFinder/comedor/'+comId)

def modificarUsuario(request):
    template = loader.get_template('FoodFinder/modificarUsuario.html')
    facultades = Facultad.objects.all()
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    context = {
        'usuario': usuarioValido,
        'facultades':facultades,
        'action': 'Modificar'
    }
    return HttpResponse(template.render(context, request))

def modificar(request):
    usuario=Usuario.objects.get(id=int(request.GET.get('usuarioId')));
    usuario.nombre = request.GET.get('nombre')
    usuario.apellido = request.GET.get('apellido')
    usuario.correo = request.GET.get('correo')
    facultad = request.GET.get('facultad')
    usuario.facultad = Facultad.objects.get(nombre = facultad)
    usuario.rol = request.GET.get('rol')
    usuario.save()
    data = {
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'correo': usuario.correo,
        'facultad': usuario.facultad.nombre,
        'rol': usuario.rol
    }

    return JsonResponse(data)
    #return redirect('/FoodFinder/cliente/')

def mostrarComentarios(request):
    template=loader.get_template('FoodFinder/comentarios.html')
    try:
        usuario = Usuario.objects.get(nombre=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuarioValido = usuario
    else:
        return redirect('FoodFinder:login')
    comentariosT = Comentario.objects.all()
    comentarios=[]
    for com in comentariosT:
        #Comentarios que aun no han sido aceptados por el moderador
        if com.aceptado == 0:
            comentarios.append(com)
    context = {
        'usuario': usuarioValido,
        'comentarios':comentarios,
    }
    return  HttpResponse(template.render(context, request))
def ajaxMostrarEditarComentario(request,idComen):
    #idCom=request.POST.get('idComentario',None)
    comentario=Comentario.objects.get(id=idComen)
    data = {
        'comedor': comentario.comedor.nombre,
        'usuario': comentario.usuario.nombreUsu,
        'comentario': comentario.comentario
    }
    return JsonResponse(data)

def cerrarSesion(request):
    logout(request)
    return redirect('FoodFinder:login')

def ajaxEliminarComentario(request, idComen):
    comentario=Comentario.objects.get(id=idComen)
    comentario.delete()
    data = {
        'msj': "Comentario eliminado correctamente"
        }
    return JsonResponse(data)
def ajaxEditarComentario(request):
    idComen=request.GET.get('idComen',None)
    coment=request.GET.get('comentario',None)
    comentario=Comentario.objects.get(id=idComen)
    comentario.comentario=coment
    comentario.save()
    data = {
        'comentario': coment
    }
    return JsonResponse(data)
def ajaxAceptarComentario(request):
    idComen=request.GET.get('idComen',None)
    comentario=Comentario.objects.get(id=idComen)
    comentario.aceptado=1;
    comentario.save()
    data = {}
    return JsonResponse(data)
