from django.db import models


# Create your models here.

class Experiencia(models.Model):
    Puesto_de_trabajo = models.CharField(max_length=50, blank=False)
    Descripcion = models.TextField(null=True)
    Nombre_de_la_empresa = models.CharField(max_length=50, blank=False)
    Fecha_de_inicio = models.DateField(blank=False, null=True)
    Fecha_de_fin = models.DateField(blank=False, null=True)


class Educacion(models.Model):

    Carrera = models.CharField(max_length=50, blank=False)
    Descripcion_educacion = models.TextField(null=True)
    Universidad = models.CharField(max_length=30, blank=False)
    Fechas_de_inicio = models.DateField(null=False)
    Fechas_de_fin = models.DateField(null=False)
