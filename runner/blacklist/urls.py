# -*- coding: utf-8 -*-
"""
Author: tony payet

Copyright: Nerim, 2015
"""
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required

from django.conf.urls import patterns, url

from blacklist.views import  blacklist_list, upload_file


urlpatterns = patterns('',
    url(r'^jsonblacklist_list/$', login_required(blacklist_list.as_view()), name='blacklist_list'),
    url(r'^csv/$', login_required(upload_file) ,name='csv'),  
)




