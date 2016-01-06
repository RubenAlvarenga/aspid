#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.template import RequestContext

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import ClientDBInfo
from django.forms.models import model_to_dict

@csrf_protect
@never_cache
def index(request):
    #fn = _fn()
    fn ='base/login.html'
    template_name = fn
    #logger.info("{0} method is loading...".format(fn))

    title = 'Home'

    if not request.user.is_authenticated():
        title = 'Login'
        form = LoginForm()
        if request.method == "POST":
            pDict =request.POST.copy()
            form = LoginForm(data=request.POST)
            if form.is_valid():
                if not request.POST.get('remember_me', None):
                    request.session.set_expiry(0)
                db = form.cleaned_data['db']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password, db=db)
                login(request, user)
                request.session['db'] = db
                request.session['database_name'] = model_to_dict(ClientDBInfo.objects.get(name=db))
                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()

                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))

                title = 'Home'
                #return render_to_response(ub.get_template(request,template_name),locals(),context_instance = RequestContext(request))
                return render_to_response(template_name, {}, context_instance=RequestContext(request, locals()))


        #return render_to_response(ub.get_template(request,'login'),locals(),context_instance = RequestContext(request))
        return render_to_response(template_name, {}, context_instance=RequestContext(request, locals()))

    if request.user.is_authenticated():
        #logger.info("{0} method is loading... done".format(fn))
        #return render_to_response(ub.get_template(request,template_name),locals(),context_instance = RequestContext(request))
        return render_to_response(template_name, {}, context_instance=RequestContext(request, locals()))




