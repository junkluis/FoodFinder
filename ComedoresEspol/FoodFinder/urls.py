from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^galeria/', views.galeria, name='galeria'),
    url(r'^comedores-cercanos/', views.comedoresC, name='comedoresC'),
    url(r'^comedores-por-facultad/', views.comedoresF, name='comedoresF'),
    url(r'^mejores-platos/', views.mejoresPlatos, name='mejoresPlatos'),
    url(r'^nosotros/', views.about, name='about'),
    url(r'^historia/', views.historia, name='historia'),
]
