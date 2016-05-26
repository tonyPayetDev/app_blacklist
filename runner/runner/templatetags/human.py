# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def humanize_time(secs):
  if secs:
    mins, secs = divmod(secs, 60);
    hours, mins = divmod(mins, 60);
    return '%02d:%02d:%02d' % (hours, mins, secs);
  else:
    return "";

@register.filter()
def humanize_price(price):
  if price:
    return "%-5.05f"%price;
  else:
    return "";
