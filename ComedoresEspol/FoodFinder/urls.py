from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^photoGallery/', views.galeria, name='galeria'),
    url(r'^comedores-cercanos/', views.comedoresC, name='comedoresC'),
    url(r'^comedoresFacultad/', views.comedoresF, name='comedoresF'),
    url(r'^mejores-platos/', views.mejoresPlatos, name='mejoresPlatos'),
    url(r'^about/', views.about, name='about'),
    url(r'^time/', views.historia, name='historia'),
    url(r'^login/', login, {'template_name':'FoodFinder/login-comd.html'}),
]
