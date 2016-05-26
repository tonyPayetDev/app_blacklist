# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <philippe.vivien@nerim.com>
Author: Tony Payet <tony@nerim.com>

Copyright: Nerim, 2014
"""
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required , user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, StreamingHttpResponse,Http404
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import python_2_unicode_compatible
from django.template import Context, loader
# Create your views here.

from blacklist.models import Blacklist
from runner.utils.logger import logger

import json
from bunch import Bunch
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import csv  


"""
retourne la data blacklist 

""" 

class blacklist_list(BaseDatatableView):
    
    model = Blacklist

    columns = ['id','type_blacklist','email','user_id']
    order_columns = ['id','type_blacklist','email','user_id']
    
    def get_context_data(self, *args, **kwargs):
        user=User.objects.get(username=self.request.user) 
        context = super(blacklist_list, self).get_context_data(**kwargs)
        data=context['data']
        data=[elem for elem in data if elem['user_id'] == user.id]

        for a in data:
            idrecup=a['id']
            a['DT_RowId']=idrecup 
            a['user_id']=str(a['user_id'] )

        blacklist=Blacklist.objects.filter(user_id=user.id )
 
        ret ={
                       'data':data,
                       'recordsTotal': blacklist.count(),
                       'recordsFiltered':  blacklist.count(),
                       'draw':	context['draw'],
                       "options": {"type_blacklist": {"blacklist":"blacklist","Bounce":"Bounce"}}
            }

        return ret

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(blacklist_list, self).dispatch(*args, **kwargs)
    
 
"""

Fonction qui va uploader un fichier csv et l'enregistrer en base qui retourne le nombre de double et le nombre de données enregistrer 

""" 

def upload_file(request):
    user=User.objects.get(username=request.user) 
    cpt=0
    cpt_doublon=0
    if request.method == 'POST':
        my_file = csv.reader(request.FILES['myfile'])
        print user.id   
        for row in my_file :

           doublon,created = Blacklist.objects.get_or_create(
                email=row[0],
                type_blacklist=row[1],
                user_id=user.id , 
                )
           if(created):
              cpt=cpt+1
           if(doublon):
              cpt_doublon=cpt_doublon+1

        return  render(request, 'app/blacklist.html',{"doublon":cpt_doublon-cpt,"created":cpt})  # todo return argument 
      
    else:
      return render(request, 'app/blacklist.html')
