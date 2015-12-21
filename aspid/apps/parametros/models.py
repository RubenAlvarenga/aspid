from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import Permission

class Empresa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    def __unicode__(self):
        return '%s' % (self.nombre)


class Aplicacion(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    icono = models.CharField(max_length=100)
    index = models.CharField(max_length=200, verbose_name='Index')
    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'
    def __unicode__(self):
        return '%s' % (self.titulo)

class Agrupador(models.Model):
    grupo = models.CharField(max_length=100, verbose_name='Grupo')
    icono = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Grupo Menu'
        verbose_name_plural = 'Grupos de Menus'
    def __unicode__(self):
        return '%s' % (self.grupo)


class Enlace(models.Model):
    app = models.ForeignKey(Aplicacion, verbose_name='App', on_delete=models.PROTECT)
    grupo = models.ForeignKey(Agrupador, verbose_name='Grupo', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100, verbose_name='Titulo')
    enlace = models.CharField(max_length=200, verbose_name='Enlace')
    permiso = models.ForeignKey(Permission, verbose_name='Permiso')
    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
    def __unicode__(self):
        return '%s' % (self.nombre)
