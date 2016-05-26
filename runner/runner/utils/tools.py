# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from __future__ import unicode_literals

import re
import inspect
from babel.numbers import format_decimal
import phonenumbers

from django.conf import settings

from runner.utils.choices import DECIMAL

#code from http://stackoverflow.com/questions/6116978/python-replace-multiple-strings
#simple et efficace
def multiple_replacer(*key_values):
    replace_dict = dict(key_values)
    replacement_function = lambda match: replace_dict[match.group(0)]
    pattern = re.compile("|".join([re.escape(k) for k, v in key_values]), re.M)
    return lambda string: pattern.sub(replacement_function, string)

def multiple_replace(string, *key_values):
    return multiple_replacer(*key_values)(string)

def format_price(price, locale='fr_fr'):
    if price == None:
        price = 0.0
        
    if type(price) <> float:
        price=float(price)
        
    if getattr(settings, 'TZ',False):
        return format_decimal(price,format='#,##0.#####;-#', locale=getattr(settings, 'TZ'))
    else:
        return format_decimal(price,format='#,##0.#####;-#', locale=locale)
    
def round_price(price):
    if price is None:
        price = 0.0
    return round(price, DECIMAL)

def infoclass2html(cls, filter=None):
    info = "<br><br>Available Class Method<br>"
    for name, data in inspect.getmembers(cls):
        if name in ('__builtins__', '__module__', '__doc__'):
            continue
        
        if filter in name:
            info += "<em><b>%s.%s</b></em><br>"%(cls.__name__, name)
    
    return info
    
def format_nat(cli):
    try:
        x = phonenumbers.parse(cli, 'FR')
        return phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
    except phonenumbers.NumberParseException:
        return cli
