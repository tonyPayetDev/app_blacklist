# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from django import template
from django.contrib.sites.models import Site

register = template.Library()

@register.simple_tag
def url_domain():
    return 'http://%s' % Site.objects.get_current().domain

@register.simple_tag
def current_domain():
    return '%s' % Site.objects.get_current().domain
