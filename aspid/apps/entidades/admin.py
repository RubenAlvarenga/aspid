#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Empresa, Persona, PersonaCliente, EmpresaCliente, Cliente

class EmpresaAdmin(admin.ModelAdmin):
	list_display=('id','nombre_real', 'nombre_comercial',)
	list_display_links=('nombre_real',)

class ClienteAdmin(admin.ModelAdmin):
	list_display=('id', Cliente, 'tipo', )
	list_display_links=(Cliente,)


admin.site.register(Persona)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(PersonaCliente)
admin.site.register(EmpresaCliente)
