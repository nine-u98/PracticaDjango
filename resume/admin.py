from django.contrib import admin

# Register your models here.

from .models import Experiencia, Educacion
admin.site.register(Experiencia)
admin.site.register(Educacion)
