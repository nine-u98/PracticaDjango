# Generated by Django 4.1.4 on 2022-12-07 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carrera', models.CharField(max_length=50)),
                ('Descripcion_educacion', models.TextField(null=True)),
                ('Universidad', models.CharField(max_length=30)),
                ('Fechas_de_inicio', models.DateField()),
                ('Fechas_de_fin', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='nom_empresa',
            new_name='Nombre_de_la_empresa',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='puesto',
            new_name='Puesto_de_trabajo',
        ),
        migrations.RemoveField(
            model_name='experiencia',
            name='fecha_fin',
        ),
        migrations.RemoveField(
            model_name='experiencia',
            name='fecha_ini',
        ),
        migrations.RemoveField(
            model_name='experiencia',
            name='titulo',
        ),
        migrations.AddField(
            model_name='experiencia',
            name='Descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='Fecha_de_fin',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='Fecha_de_inicio',
            field=models.DateField(null=True),
        ),
    ]
