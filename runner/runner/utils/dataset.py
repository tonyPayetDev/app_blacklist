# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from __future__ import unicode_literals

from copy import deepcopy

from django.db.models.query import QuerySet
from django.core.serializers.base import DeserializedObject
from runner.utils.choices import BIZ_LIST, ZONE_LIST, get_zone

from runner.utils.logger import logger
import re
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

        
def parse_data_list(data, k, valname='val'):
    return [{'id': re.search(r'\[(\d+)\]', key).group(1), 
             valname: data[key]} 
            for key in data.keys() 
            if  k in key and data[key]]
    
    
def formatdataT(data):
    
#
#    name =data['data[name]']
#    indicatif = data['data[indicatif]']
#    code = data['data[code]']
#    zone = data['data[zone]']
    
#    juri = [{'id': id_price, 'price_p': price}  
#            for id_price, price in parse_data_list(data, 'juripurchases').items() 
#            if price]
##    
#    for id_price, price in parse_data_list(data, 'juripurchases').items():
#        if price:
#            juri.append( {
#                        "id": id_price,
#                        "price_p": price,
#                    } )
#    
    print data
    search_data = re.compile(r'data\[(\w+)\]') 
    for k in data.keys():
        print "aaaa"
        print k
        if 'data' in k:
            print search_data.search(k).group(1), data[k]
        else :
            print k
        
    return {'indicatif': data['data[indicatif]'], 
            'name': data['data[name]'],
            'code': data['data[code]'],
            'zone':get_zone(data['data[zone]']),
            'juripurchase': parse_data_list(data, 'juripurchases', 'price_p')}


def format_datatable(request, withrowid=True):
    data = {'data':{}}
    
    for x in request:
        logger.debug("Working %s=%s"%(x, request.get(x)))
        
        if x == 'id' and not data['data'].has_key('id') and withrowid==True:
            m='id'
        elif x.startswith('data['):
            m=x[x.find("[")+1:x.find("]")]
            #if len(m) == 0 and not data['data'].has_key('id') and withrowid==True:
            #    m='id'
        elif x.startswith('id['):
            m=x[x.find("[")+1:x.find("]")]
            if len(m) == 0 and not data['data'].has_key('id') and withrowid==True:
                m='id'
        else:
            continue
            
        data['data'][m] = request.get(x)
        logger.debug("data %s=%s"%(m, data['data'][m]))
    
    logger.debug("data %s"%data)
    return data

