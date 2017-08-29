# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Facultad)
admin.site.register(Comedor)
admin.site.register(Platillo)
admin.site.register(Usuario)
admin.site.register(Denuncia)
admin.site.register(Comentario)
