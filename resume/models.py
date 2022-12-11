from django.db import models


# Create your models here.


class Experience(models.Model):
    workstation = models.CharField(max_length=50, blank=False, verbose_name='Puesto de trabajo')
    description = models.TextField(null=True, verbose_name='Descripcion')
    company = models.CharField(max_length=50, blank=False, verbose_name='Empresa', default='')
    start_date = models.DateField(blank=False, null=True, verbose_name='Fecha de inicio')
    ending_date = models.DateField(blank=False, null=True, verbose_name='Fecha de finalizacion')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
        ordering = ['created']

    def __str__(self):
        return self.workstation


class Education(models.Model):
    career = models.CharField(max_length=50, blank=False)
    description = models.TextField(null=True)
    university = models.CharField(max_length=30, blank=False)
    start_date = models.DateField(null=False)
    ending_date = models.DateField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Educación'
        verbose_name_plural = 'Estudios'
        ordering = ['created']

    def __str__(self):
        return self.career
