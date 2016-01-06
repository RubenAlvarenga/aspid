#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from middlewares import RequestAddSessionVars

def change_database(request):
    RequestAddSessionVars.process_view(request, )
    return render_to_response(self.template_name, {}, context_instance=RequestContext(request, locals()))

class IndexView(View):
    template_name='index.html'
    def get(self, request):
        return render_to_response(self.template_name, {}, context_instance=RequestContext(request, locals()))




