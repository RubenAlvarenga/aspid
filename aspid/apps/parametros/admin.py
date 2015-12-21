#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Empresa, Aplicacion, Enlace, Agrupador


admin.site.register(Empresa)
admin.site.register(Aplicacion)
admin.site.register(Enlace)
admin.site.register(Agrupador)
