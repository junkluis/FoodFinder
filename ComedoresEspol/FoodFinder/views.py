# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import date
from FoodFinder.models import *

def index(request):
    template = loader.get_template('FoodFinder/index.html')
    platillos = Platillo.objects.all()
    context = {
        'platillos':platillos,
    }
    return HttpResponse(template.render(context, request))

def galeria(request):
    template = loader.get_template('FoodFinder/photoGallery.html')
    context = {}
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
