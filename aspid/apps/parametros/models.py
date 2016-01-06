from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import Permission



from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

#from ezerve.utils import gv



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





AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class ClientDBInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('DB Name'), help_text=_('Enter a Database name which is available to client'))
    display_name = models.CharField(max_length=255, verbose_name=_('DB Display Name'), help_text=_('Enter a Database display name which is for lable'))
    color_back = models.CharField(max_length=12, verbose_name=_('Color de Fondo'), help_text=_('Ingresa el color caracteristico'))
    # logo = models.ImageField(upload_to='clientlogo', default='clientlogo/no_clientphoto.png', blank=True)
    # contact_address_line1 = models.CharField(max_length=140, blank=True)
    # contact_address_line2 = models.CharField(max_length=140, blank=True)
    # contact_address_line3 = models.CharField(max_length=140, blank=True)
    # city = models.CharField(max_length=140, blank=True)
    # country = models.ForeignKey(Country)
    # state = models.CharField(max_length=140, blank=True)
    # zipcode = models.IntegerField(default=0)
    # latitude = models.FloatField(default=0.0)
    # longitude = models.FloatField(default=0.0)

    # created = models.DateTimeField(default=timezone.now, auto_now_add=True)
    # modified = models.DateTimeField(default=timezone.now, auto_now=True)
    created_by = models.ForeignKey(AUTH_USER_MODEL,related_name = "%(class)s_createdby")
    updated_by = models.ForeignKey(AUTH_USER_MODEL, related_name = "%(class)s_updatedby")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('ClientDBInfo')
        verbose_name_plural = _('ClientDBInfos')
        ordering = ('name',)