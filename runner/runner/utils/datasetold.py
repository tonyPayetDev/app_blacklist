# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from __future__ import unicode_literals

from copy import deepcopy

from django.db.models.query import QuerySet
from django.core.serializers.base import DeserializedObject

from runner.utils.logger import logger

def duplicate_query_sets(classname, queryset, **kwargs):
    """
    Copy un queryset (format queryset ou serialize)
    TODO: verification des champs m2m ou fk a faire pour la copie
    Les queryset sont passes directement depuis les api django, les
    serialize pour utilisation des tasks celery (json)
    """
    logger.info("queryset=%s (%s) kwargs=%s (%s)"%(
                queryset, type(queryset),  kwargs, type(kwargs)))
    for p in queryset:
        if type(p) == DeserializedObject:
            p=p.object
        
        id = p.id
        p = classname.objects.get(id=id)
        newp = deepcopy(p)
        logger.info("id=%s p=%s newp=%s"%(id, p.__dict__, newp.__dict__))
                
        newp.pk = None
        for i, v in kwargs.iteritems():
            logger.info("i=%s v=%s"%(i, v))
            setattr(newp, i, v)
        newp.save()



def duplicatem2m_query_sets(queryset, **kwargs):
    logger.debug("queryset=%s (%s) kwargs=%s (%s)"%(
                queryset, type(queryset),  kwargs, type(kwargs)))
    
    for p in queryset:
        newp = deepcopy(p)
        newp.pk=None
        newp.save()
        
