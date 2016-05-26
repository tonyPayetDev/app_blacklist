# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2015
"""
from __future__ import unicode_literals

from django.conf.urls import url, include

from rest_framework import routers

from .views import  JuridictionViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'juridt', JuridictionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^docs/', include('rest_framework_swagger.urls')),
]
