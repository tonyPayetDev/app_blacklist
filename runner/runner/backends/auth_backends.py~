# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014/2015

Auth avec gestion du SITE_ID
La partie permission doit etre reimplementee ici car le backend est\
un object et non un ModelBackend
"""
from __future__ import unicode_literals



from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from runner.utils.logger import logger
from runner.utils.site import the_site


class RunnerUserModelBackend(object):
    def authenticate(self, username=None, password=None):
        logger.info('{0} {1}'.format(self, username))
        
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                if user.check_password(password):
                    return user
                else:
                    logger.error('SuperUser access {0} {1}'.format(self, username))
                    return None
            
            try:
                if user.runneruser:
                    logger.info('RunnerUser:{0} current site:{1} user site:{2}'.
                    format(username, the_site(), user.runneruser.site.id))
                    if the_site() == user.runneruser.site.id:
                        if user.check_password(password):
                            return user
            except:
                logger.error('RunnerUser access {0} {1}'.format(self, username))
                return None
        except User.DoesNotExist:
            logger.error('User Not Found {0} {1}'.format(self, username))
            return None

    def get_user(self, user_id):
        logger.info('{0} {1}'.format(self, user_id))
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            logger.error('User Not Found {0} {1}'.format(self, user_id))
            return None

    def _get_user_permissions(self, user_obj):
        return user_obj.user_permissions.all()

    def _get_group_permissions(self, user_obj):
        user_groups_field = get_user_model()._meta.get_field('groups')
        user_groups_query = 'group__%s' % user_groups_field.related_query_name()
        return Permission.objects.filter(**{user_groups_query: user_obj})

    def _get_permissions(self, user_obj, obj, from_name):
        """
        Returns the permissions of `user_obj` from `from_name`. `from_name` can
        be either "group" or "user" to return permissions from
        `_get_group_permissions` or `_get_user_permissions` respectively.
        """
        if not user_obj.is_active or user_obj.is_anonymous() or obj is not None:
            return set()

        perm_cache_name = '_%s_perm_cache' % from_name
        if not hasattr(user_obj, perm_cache_name):
            if user_obj.is_superuser:
                perms = Permission.objects.all()
            else:
                perms = getattr(self, '_get_%s_permissions' % from_name)(user_obj)
            perms = perms.values_list('content_type__app_label', 'codename').order_by()
            setattr(user_obj, perm_cache_name, set("%s.%s" % (ct, name) for ct, name in perms))
        return getattr(user_obj, perm_cache_name)

    def get_user_permissions(self, user_obj, obj=None):
        """
        Returns a set of permission strings the user `user_obj` has from their
        `user_permissions`.
        """
        return self._get_permissions(user_obj, obj, 'user')

    def get_group_permissions(self, user_obj, obj=None):
        """
        Returns a set of permission strings the user `user_obj` has from the
        groups they belong.
        """
        return self._get_permissions(user_obj, obj, 'group')

    def get_all_permissions(self, user_obj, obj=None):
        if not user_obj.is_active or user_obj.is_anonymous() or obj is not None:
            return set()
        if not hasattr(user_obj, '_perm_cache'):
            user_obj._perm_cache = self.get_user_permissions(user_obj)
            user_obj._perm_cache.update(self.get_group_permissions(user_obj))
        return user_obj._perm_cache

    def has_perm(self, user_obj, perm, obj=None):
        if not user_obj.is_active:
            return False
        return perm in self.get_all_permissions(user_obj, obj)

    def has_module_perms(self, user_obj, app_label):
        """
        Returns True if user_obj has any permissions in the given app_label.
        """
        if not user_obj.is_active:
            return False
        for perm in self.get_all_permissions(user_obj):
            if perm[:perm.index('.')] == app_label:
                return True
        return False
        
    
