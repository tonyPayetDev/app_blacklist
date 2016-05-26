# -*- coding: utf-8 -*-

# Copyright (C) 2014 Nerim (Philippe 'paHpa' Vivien)

from __future__ import unicode_literals

from datetime import datetime
import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.db.models import Q
from django.conf import settings

from django_datatables_view.base_datatable_view import BaseDatatableView



from runner.utils.logger import logger
from runner.utils.choices import ZONE_JSONLIST, BIZ_JSONLIST

#@login_required(login_url='/account/login/')
@login_required
def home(request):
    """
    TODO: Doc
    """

#    return render(request, 'home.html')
    return TemplateResponse(request, 'app/blacklist.html', {'logo':'TEST PAHPA'}).render()

    
def empty_view(request, *args, **kwargs):
    return HttpResponse('')



def my_custom_404_view(request):
    r=render(request, 'runner404.html')
    logger.info("r=%s"%r.__dict__)
    return r

