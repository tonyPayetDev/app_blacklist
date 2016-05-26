# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>

Copyright: Nerim, 2014
"""
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

MINUTE = 60
DECIMAL = 5

NAT ='N'
SPEINT = 'P'
CONTEXTTELCO = 'Telco'
CONTEXTRESELLER = 'Resel'
INTERMEDIATION = "INTERMEDIATION"

TYPEJURI = {NAT:'N',SPEINT:'P'}
INFOJURI = {NAT:'National',SPEINT:'Spe/International'}
VALOCONTEXT = {CONTEXTTELCO:'Telco', CONTEXTRESELLER:'Reseller'}

RUNNERWORK_CHOICES = (
    ('D', _('Debug')), 
    ('G', _('Getfile')),
    ('0', _('ImportCdr')),
    ('1', _('SetCdr')),
    ('2', _('ValoCdr')),
    ('3', _('BillCdr')),
    ('4', _('Export')),
)
RUNNERWORK_JSONLIST = sorted([{k:"%s"%unicode(v)} for (k, v) in RUNNERWORK_CHOICES])

CONTEXT_CHOICES = (
    ('T', _('Telco')),
    ('R', _('Reseller'), )
)	
CONTEXT_JSONLIST = sorted([{k:"%s"%unicode(v)} for (k, v) in CONTEXT_CHOICES])

STATUS_VALO = CONTEXT_CHOICES +(
    ('C', _('Client')),
)	
STATUS_VALO_JSONLIST = sorted([{k:"%s"%unicode(v)} for (k, v) in STATUS_VALO])

BIZ_CHOICES = (
    ('P', _('Presel')),
    ('V', _('Vga/Vgast')),
    ('T', _('Toip')),
    ('C', _('Centrex')),
    ('M', _('Mvno')),
    ('W', _('WholeSale')),
    ('8', _('0800 Rev.')),
    ('O', _('Other')),
)	
BIZ_LIST = sorted([(k, "%s"%unicode(v)) for (k, v) in BIZ_CHOICES])
BIZ_JSONLIST = sorted([{k:"%s"%unicode(v)} for (k, v) in BIZ_CHOICES])

ZONE_CHOICES = (
    ('N', _('National')),
    ('I', _('International')),
    ('S', _('Special')),
    ('P', _('International+Special')),
)
ZONE_LIST = sorted([(k,"%s"%unicode(v)) for (k, v) in ZONE_CHOICES])
ZONE_JSONLIST = sorted([{k:"%s"%unicode(v)} for (k, v) in ZONE_CHOICES])

PHONEKIND_CHOICES = (
    ('F', _('Fixe')),
    ('M', _('Mobile'))
)
PHONEKIND_LIST = sorted([(k,"%s"%unicode(v)) for (k, v) in PHONEKIND_CHOICES])
PHONEKIND_JSONLIST = sorted([{k:"%s"%unicode(v)} for (k, v) in PHONEKIND_CHOICES])

TYPECDR_CHOICES = (
	('C', _('Com')),
	('S', _('Service')),
)
TYPECDR_LIST = sorted([(k,"%s"%unicode(v)) for (k, v) in TYPECDR_CHOICES])
TYPECDR_JSONLIST = sorted([{k:"%s"%unicode(v)} for (k, v) in TYPECDR_CHOICES])


#provient d'info normaction
#TODO reprise pour l'intégration, sera change
CONTRACT_STATUS = (
    ('0', u'Prospect'), 
    ('10', u'adv_Création'), 
    ('20', u'Tec_affectation'), 
    ('25', u'Tec_Prise_Rdv'), 
    ('30', u'Tec_Cmd_Vga'), 
    ('40', u'Tec_Audit'), 
    ('45', u'Tec_Retour_Vga'), 
    ('50', u'Tec_Déploiement'), 
    ('60', u'Fac_EnCours'), 
    ('70', u'Tec_FinDéploiement'), 
    ('80', u'ACTIF'), 
    ('104', u'Résiliation_EnCours'), 
    ('106', u'Tec_Résliation'), 
    ('107', u'Adm_Résil'), 
    ('110', u'Terminé'), 
    ('112', u'Résilié'), 
    ('1000', u'Retour_Commerce'), 
    ('1010', u'Envoi_contentieux'), 
    ('1110', u'Annulé'), 
    ('1200', u'Annulé_Remplacé'), 
    ('1210', u'Attente_Leaseur')
)
CONTRACT_STATUS_JSONLIST = sorted([{k:"%s"%unicode(v)} for (k, v) in CONTRACT_STATUS])

# RFC 5424 defines eight severity levels
SEVERITYLEVEL_CHOICES = (
    ('0', _('Emergency')), 
    ('1', _('Alert')),
    ('2', _('Critical')),
    ('3', _('Error')),
    ('4', _('Warning')),
    ('5', _('Notice')),
    ('6', _('Informational')),
    ('7', _('Debug'))
)

def info_bizzone():
    return "\n".join(["(%s) %s"%(k, unicode(v)) for (k, v) in BIZ_CHOICES])

def list_bizzone():
    return ["%s"%k for (k, v) in BIZ_CHOICES]

def info_typecdr():
    return "\n".join(["(%s) %s"%(k, unicode(v)) for (k, v) in TYPECDR_CHOICES])

def list_typecdr():
    return ["%s"%k for (k, v) in TYPECDR_CHOICES]

def info_runnerwork():
    return "\n".join(["(%s) %s"%(k, unicode(v)) for (k, v) in RUNNERWORK_CHOICES])

def list_runnerwork():
    return ["%s"%k for (k, v) in RUNNERWORK_CHOICES]

def get_runnerwork(value):
    for k, v in RUNNERWORK_CHOICES:
        if v==value:
            return k
    return None

def info_contratstatus():
    return "\n".join(["(%s) %s"%(k, unicode(v)) for (k, v) in CONTRACT_STATUS])

def list_contratstatus():
    return ["%s"%k for (k, v) in CONTRACT_STATUS]

def get_contratstatus(key):
    for k, v in CONTRACT_STATUS:
        if k==key:
            return v
    
    return None

def get_zone(value):
    for k, v in ZONE_CHOICES:
        if v==value:
            return k
    return None
