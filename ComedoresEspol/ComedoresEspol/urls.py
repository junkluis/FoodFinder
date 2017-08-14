from django.conf.urls import url, include
from django.contrib import admin
from FoodFinder import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^FoodFinder/', include('FoodFinder.urls')),
    url(r'^', include('FoodFinder.urls')),
]
