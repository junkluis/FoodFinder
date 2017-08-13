from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from FoodFinder import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^FoodFinder/', include('FoodFinder.urls')),
    url(r'^', include('FoodFinder.urls')),
    url(r'^denuncias/', views.DenunciaList.as_view()),
    url(r'^denuncias/(?P<pk>[0-9]+)/', views.DenunciaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)