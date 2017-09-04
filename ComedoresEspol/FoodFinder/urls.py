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
    url(r'^login/', views.loginUser, name='login'),
    url(r'^contacto/',views.contacto,name='contacto'),
    url(r'^refresh/$', views.ajaxMejoresPlatos, name='ajaxPlatos'),
    url(r'^valorar/$', views.ajaxValorar, name='ajaxValorar'),
    url(r'^valoracion/$', views.valoracion, name='valoracion'),
    url(r'^denuncia/$', views.denuncia, name='denuncia'),
    url(r'^guardarDenuncia/$', views.guardarDenuncia, name='guardarDenuncia'),
    url(r'^pruebas/$', views.guardarDenuncia, name='pruebas'),
    url(r'^moderador/$', views.sesionModerador, name='moderador'),
    url(r'^admin/$', views.sesionAdmin, name='admin'),
    url(r'^admin/actualizarInfo$', views.actualizarInfoAdmin, name='actualizarInfo'),
    url(r'^cliente/$', views.sesionCliente, name='cliente'),
    url(r'^cliente/modificarUsuario$', views.modificar, name='modificarUsuario'),
    url(r'^platillo/(?P<pId>[0-9]+)$', views.platilloInfo, name='platillo'),
    url(r'^comedor/(?P<comId>[0-9]+)$', views.comedorInfo, name='comedor'),
    url(r'^guardarComentario/$', views.guardarComentario, name='guardarComentario'),
    url(r'^modificar/$', views.modificar, name='modificar'),
    url(r'^cerrarSesion/$', views.cerrarSesion, name='cerrarSesion'),
    url(r'^comentarios/$', views.mostrarComentarios, name='comentarios'),
    url(r'^mostrarEditarComentario/(?P<idComen>[0-9]+)$', views.ajaxMostrarEditarComentario, name='mostrarEditarComentario'),
    url(r'^eliminarComentario/(?P<idComen>[0-9]+)$', views.ajaxEliminarComentario, name='eliminarComentario'),
    url(r'^editarComentario/$', views.ajaxEditarComentario, name='editarComentario'),
    url(r'^aceptarComentario/$', views.ajaxAceptarComentario, name='aceptarComentario'),
]
