# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0003_clientdbinfo_color_back'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdbinfo',
            name='color_back',
            field=models.CharField(blank=True, help_text='Ingresa el color caracteristico', max_length=12, null=True, verbose_name='Color de Fondo'),
        ),
    ]
