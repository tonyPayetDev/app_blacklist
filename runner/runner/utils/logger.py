# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from __future__ import unicode_literals

import logging

logger = logging.getLogger('runner')

def logdebug():
    """
    set debug logger
    """
    logger.setLevel(logging.DEBUG)
    
def loginfo():
    """
    set info logger
    """
    logger.setLevel(logging.INFO)


def logdashboard(func):
    def wrapper(*args, **kwargs):
        logger.info("%s %s"%(args, kwargs))
        ret =  func(*args, **kwargs)
        logger.info("RET %s"%ret)
        return ret
    return wrapper
