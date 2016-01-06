#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

#from apps
from .models import ClientDBInfo

class LoginForm(forms.Form):
    ClientDB = ClientDBInfo.objects.all()
    db_choice_list = []
    for db in ClientDB:
        db_choice_list.append((db.name, db.display_name))


    db = forms.ChoiceField(choices=db_choice_list, widget=forms.Select(attrs = {'class':'form-control input-lg'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class' : 'form-control input-lg', 'placeholder' : "User"}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(render_value=False, attrs={'class' : 'form-control input-lg', 'placeholder' : "Password"}))

    def clean(self):
        if ('username' in self.cleaned_data and 'password' in self.cleaned_data):
            db = self.cleaned_data['db']
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = authenticate(username=username, password=password, db=db)

            if user is not None:
                if not user.is_active:
                    raise forms.ValidationError(_('Your account is not active, please contact the site admin.'))
            else:
                raise forms.ValidationError(_('Please enter a correct username and password. Note that both fields are case-sensitive'))

        return self.cleaned_data