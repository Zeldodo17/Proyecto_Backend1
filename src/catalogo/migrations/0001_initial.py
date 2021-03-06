# Generated by Django 3.2.7 on 2021-10-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='usuarios', verbose_name='Imagen de perfil')),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Clasificación',
                'verbose_name_plural': 'Clasificaciónes',
            },
        ),
        migrations.CreateModel(
            name='Herramientas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='usuarios', verbose_name='Imagen de perfil')),
                ('clasificacion', models.ManyToManyField(to='catalogo.Clasificacion')),
            ],
            options={
                'verbose_name': 'Herramienta',
                'verbose_name_plural': 'Herramientas',
            },
        ),
    ]
