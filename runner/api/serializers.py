# -*- coding: utf-8 -*-
"""
Author: tony ' payet <tony.payet.professionnel@.com>

Copyright: Nerim, 2015
"""
from __future__ import unicode_literals

from rest_framework import serializers


from blacklist.models import Blacklist


from runner.utils.logger import logger
from runner.utils.choices import BIZ_LIST, ZONE_LIST, PHONEKIND_LIST

from rest_framework.renderers import JSONRenderer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class JuridictionSerializer(serializers.ModelSerializer):


    def create(self, validated_data): 
        """
        Update and return a new `juridiction` instance, given the validated data.
        """
        user=User.objects.get(username=validated_data.get('user')) 

        post=Blacklist.objects.create(user_id=user.id)
        post.email = validated_data.get('email')
        post.type_blacklist = validated_data.get('type_blacklist')

        post.save()
        return post
    
    def update(self, instance, validated_data):
        """
        Update and return a new `juridiction` instance, given the validated data.
        """
  
        post = Blacklist.objects.get(pk=instance.pk)
        post.email = validated_data.get('email')
        post.type_blacklist = validated_data.get('type_blacklist')

        post.save()
        return post
        
    class Meta:
        model = Blacklist
        fields = (
                    'id',
                    'email',
                    'type_blacklist',
                    'user',

                )
        


