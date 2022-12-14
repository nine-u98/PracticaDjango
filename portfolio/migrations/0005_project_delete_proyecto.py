# Generated by Django 4.1.4 on 2022-12-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_proyecto_imagen_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Titulo')),
                ('tags', models.CharField(choices=[('API', 'APIS'), ('django', 'DJANGO'), ('flask', 'FLASK'), ('scripts', 'SCRIPTS')], default='API', max_length=7, verbose_name='Tags')),
                ('image_url', models.URLField(default='None', verbose_name='Imagen url')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['created'],
            },
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]
