# Generated by Django 4.1.4 on 2022-12-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_proyecto_img_proyecto_imagen_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='Imagen_url',
            field=models.URLField(default='None'),
        ),
    ]
