# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from __future__ import unicode_literals

from django.contrib.sites.models import Site
from django.contrib.sites.models import get_current_site
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

def the_site():
    try:
#        return Site.objects.get_current()
#    except:
        return settings.SITE_ID
    except:
        return 1
    
def site_name():
    try:
        return Site.objects.get_current()
    except:
        return settings.SITE_ID

