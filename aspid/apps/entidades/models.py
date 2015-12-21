#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models



class Empresa(models.Model):
    nombre_real=models.CharField(max_length=100, verbose_name='Nombre Real')
    nombre_comercial=models.CharField(max_length=100, verbose_name='Nombre Comercial')
    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'
        ordering=['nombre_real']
        default_permissions = ('add', 'change', 'delete', 'view', 'list')

    def __unicode__(self):
        return unicode(self.nombre_real)

    def save(self, *args, **kwargs):
        nombre_real = getattr(self, 'nombre_real', False)
        if nombre_real: setattr(self, 'nombre_real', nombre_real.title())
        nombre_comercial = getattr(self, 'nombre_comercial', False)
        if nombre_comercial: setattr(self, 'nombre_comercial', nombre_comercial.title())
        super(Empresa, self).save(*args, **kwargs)


class Persona(models.Model):
    cedula=models.CharField(max_length=10, verbose_name='Cédula', unique=True)
    nombre1=models.CharField(max_length=50, verbose_name='Nombre')
    nombre2=models.CharField(max_length=50, verbose_name='Segundo Nombre', blank=True)
    apellido1=models.CharField(max_length=50, verbose_name='Primer Apellido')
    apellido2=models.CharField(max_length=50, verbose_name='Segundo Apellido', blank=True)
    fecha_nacimiento=models.DateField(verbose_name='Fecha Nacimiento', blank=True, null=True)
    empresa=models.ForeignKey(Empresa, null=True, blank=True)
    
    @property
    def get_full_name(self):
        if self.apellido2=='': return self.apellido1 +", "+ self.nombre1 +" "+ self.nombre2
        else: return self.apellido1 +" "+ self.apellido2 +', '+ self.nombre1 +" "+ self.nombre2

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
        ordering =[ 'apellido1', 'apellido2', 'nombre1']
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        
    def __unicode__(self):
        return '%s, %s' % (self.apellido1, self.nombre1)
    def save(self, *args, **kwargs):
        nombre1 = getattr(self, 'nombre1', False)
        if nombre1: setattr(self, 'nombre1', nombre1.title())
        nombre2 = getattr(self, 'nombre2', False)
        if nombre2: setattr(self, 'nombre2', nombre2.title())
        apellido1 = getattr(self, 'apellido1', False)
        if apellido1: setattr(self, 'apellido1', apellido1.title())
        apellido2 = getattr(self, 'apellido2', False)
        if apellido2: setattr(self, 'apellido2', apellido2.title())        
        super(Persona, self).save(*args, **kwargs)




class Cliente(models.Model):
    ruc=models.CharField(max_length=10, verbose_name='Ruc')
    @property
    def tipo(self):
        try:
            nombre=PersonaCliente.objects.get(pk=self.id)
            nombre='Persona'
        except:
            nombre=EmpresaCliente.objects.get(pk=self.id)
            nombre='Empresa'
        return str(nombre)
    @property
    def nombre(self):
        try: nombre=PersonaCliente.objects.get(pk=self.id)
        except: nombre=EmpresaCliente.objects.get(pk=self.id)
        return unicode(nombre)
    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'

    def __unicode__(self):
        try:
            nombre=PersonaCliente.objects.get(pk=self.id)
            nombre=str(nombre.Persona.apellido1)+', '+str(nombre.persona.nombre1)
        except:
            nombre=EmpresaCliente.objects.get(pk=self.id)
            nombre=nombre.Empresa.nombre_real
        return str(nombre)


class PersonaCliente(Cliente):
    persona=models.OneToOneField(Persona)
    class Meta:
        verbose_name = 'cliente persona'
        verbose_name_plural = 'clientes personas'
    def __unicode__(self):
        return '%s, %s' % (self.Persona.apellido1, self.Persona.nombre1)
    def save(self, *args, **kwargs):
        super(PersonaCliente, self).save(*args, **kwargs)


class EmpresaCliente(Cliente):
    empresa=models.OneToOneField(Empresa)
    class Meta:
        verbose_name = 'cliente empresa'
        verbose_name_plural = 'clientes empresas'
    def __unicode__(self):
        return self.Empresa.nombre_real
    def save(self, *args, **kwargs):
        super(EmpresaCliente, self).save(*args, **kwargs)

# class ViewCliente(models.Model):
#     ruc=models.CharField(max_length=10, blank=True, verbose_name='Ruc')
#     tipo=models.CharField(max_length=10, blank=True, verbose_name='Tipo')
#     nombre=models.CharField(max_length=100, verbose_name='Nombre')
#     class Meta:
#         managed = False
#         verbose_name='cliente'
#         verbose_name_plural='clientes'
