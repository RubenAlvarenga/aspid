# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agrupador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=100, verbose_name='Grupo')),
                ('icono', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Grupo Menu',
                'verbose_name_plural': 'Grupos de Menus',
            },
        ),
        migrations.CreateModel(
            name='Aplicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('icono', models.CharField(max_length=100)),
                ('index', models.CharField(max_length=200, verbose_name='Index')),
            ],
            options={
                'verbose_name': 'App',
                'verbose_name_plural': 'Apps',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Enlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Titulo')),
                ('enlace', models.CharField(max_length=200, verbose_name='Enlace')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parametros.Aplicacion', verbose_name='App')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parametros.Agrupador', verbose_name='Grupo')),
                ('permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission', verbose_name='Permiso')),
            ],
            options={
                'verbose_name': 'Enlace',
                'verbose_name_plural': 'Enlaces',
            },
        ),
    ]
