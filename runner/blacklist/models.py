from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User



@python_2_unicode_compatible
class Blacklist(models.Model):
    email = models.CharField(max_length=200)
    type_blacklist = models.CharField(max_length=200)
    user = models.ForeignKey(User)    
    
    class Meta:
        verbose_name = 'Blacklist'
    
    def __str__(self):              # __unicode__ on Python 2
        return self.email
        

