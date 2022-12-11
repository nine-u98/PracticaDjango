# Generated by Django 4.1.4 on 2022-12-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_educacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('university', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Educación',
                'verbose_name_plural': 'Estudios',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workstation', models.CharField(max_length=50, verbose_name='Puesto de trabajo')),
                ('description', models.TextField(null=True, verbose_name='Descripcion')),
                ('university', models.CharField(max_length=50, verbose_name='Universidad')),
                ('start_date', models.DateField(null=True, verbose_name='Fecha de inicio')),
                ('ending_date', models.DateField(null=True, verbose_name='Fecha de finalizacion')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
                'ordering': ['created'],
            },
        ),
        migrations.DeleteModel(
            name='Educacion',
        ),
        migrations.DeleteModel(
            name='Experiencia',
        ),
    ]