from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


app_name = 'FoodFinder'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^photoGallery/', views.galeria, name='galeria'),
    url(r'^comedores-cercanos/', views.comedoresC, name='comedoresC'),
    url(r'^comedoresFacultad/', views.comedoresF, name='comedoresF'),
    url(r'^mejores-platos/', views.mejoresPlatos, name='mejoresPlatos'),
    url(r'^about/', views.about, name='about'),
    url(r'^time/', views.historia, name='historia'),
    url(r'^login/', views.login, name='login'),
    url(r'^contacto/',views.contacto,name='contacto'),
    url(r'^refresh/$', views.ajaxMejoresPlatos, name='ajaxPlatos'),
    url(r'^valorar/$', views.ajaxValorar, name='ajaxValorar'),
    url(r'^valoracion/$', views.valoracion, name='valoracion'),

]
