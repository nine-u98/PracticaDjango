from django.db import models


# Create your models here.
class About(models.Model):
    curriculum = models.FileField(verbose_name='Curriculum PDF', upload_to='curriculum')

    class Meta:
        verbose_name = 'PDF'
        verbose_name_plural = 'PDFS'
