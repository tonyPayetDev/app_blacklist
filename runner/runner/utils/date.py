# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from __future__ import unicode_literals

from datetime import datetime
import dateutil.relativedelta

from django.utils import timezone
from django.conf import settings

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_DATE_FORMAT = "%d/%m/%Y"
DATE_HEURE_FORMAT = "%H:%M:%S"
DATE_FORMAT_CDR = '%Y%m%d%H%M%S'
DATE_FORMAT_FR = "%d/%m/%Y %H:%M:%S"

def print_current_datefr():
    dt = datetime.now()
    return dt.strftime(DATE_FORMAT_FR)
    
def datefromstring(buf, short=True):
    if short:
        return datetime.strptime(buf, DATE_DATE_FORMAT)
    
    return datetime.strptime(buf, DATE_FORMAT)

def dateformatcdr(buf):
    return datetime.strptime(buf, DATE_FORMAT_CDR)

def datenow():
    """
    return now() with timezone aware from TZ setting or datetime
    """
    if getattr(settings, 'USE_TZ') == True:
        return timezone.make_aware(datetime.now(),timezone.get_default_timezone())
    else:
        return datetime.now()
    
def dt2ts(dt):
    """
    DateTime To TimeStamp
    """
    return int(dt.strftime("%s"))

def ts2dt(ts, timeplus=0):
    """
    TimeStamp To DateTime
    """
    if getattr(settings, 'USE_TZ') == True:
        return timezone.make_aware(datetime.fromtimestamp(ts+timeplus),timezone.get_default_timezone())
    else:
        return datetime.fromtimestamp(ts+timeplus)

def ctime2dt(ct):
    return datetime.strptime(ct, "%a %b %d %H:%M:%S %Y")

def dateofdate(dt):
    return dt.strftime(DATE_DATE_FORMAT)

def hourofdate(dt):
    return dt.strftime(DATE_HEURE_FORMAT)

def yearofdate(dt):
    return dt.year

def monthofdate(dt):
    return dt.month
    
def dayofdate(dt):
    return dt.day

def prevmonthofdate(dt):
    dtp = dt + dateutil.relativedelta.relativedelta(months=-1)
    return dtp.month 

def prevyearofdate(dt):
    dtp = dt + dateutil.relativedelta.relativedelta(months=-1)
    return dtp.year
