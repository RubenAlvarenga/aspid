#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission


class MyBackend(object):
    """
    Authenticates against django.contrib.auth.models.User.
    """

    def authenticate(self, username=None, password=None, db=None, **kwargs):

        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel.objects.using(db).get(username=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None


    def get_user(self, user_id):
        UserModel = get_user_model()

        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None