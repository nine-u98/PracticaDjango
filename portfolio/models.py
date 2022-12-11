from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=120, verbose_name='Titulo')
    API = 'API'
    DJANGO = 'django'
    FLASK = 'flask'
    SCRIPT = 'scripts'
    CAT_CHOICES = [
        (API, 'APIS'),
        (DJANGO, 'DJANGO'),
        (FLASK, 'FLASK'),
        (SCRIPT, 'SCRIPTS'),
    ]
    tags = models.CharField(
        max_length=7,
        choices=CAT_CHOICES,
        default=API,
        verbose_name='Tags'
    )
    image_url = models.URLField(blank=False, default="", verbose_name='Imagen url')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['created']

    def __str__(self):
        return self.title
