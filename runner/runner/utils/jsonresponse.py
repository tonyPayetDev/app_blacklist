# -*- coding: utf-8 -*-

# Copyright (C) 2015 Nerim (Philippe 'paHpa' Vivien)

from __future__ import unicode_literals

from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer

from runner.utils.logger import logger

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
