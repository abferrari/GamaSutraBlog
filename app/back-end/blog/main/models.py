# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.timezone import localtime


# Create your models here.
class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    timestamp = models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField(unpack_ipv4=True)


    @staticmethod
    def list():
        lead_list = []

        for lead in Lead.objects.all():
            reg = {
                'full_name': lead.first_name + ' ' + lead.last_name,
                'email': lead.email,
                'date': localtime(lead.timestamp).strftime('%d/%m/%Y'),
                'hour': localtime(lead.timestamp).strftime('%H:%M:%S'),
                'IP': lead.ip,
            }
            csv = '{full_name},{email},{date},{hour},{IP}'.format(**reg)
            lead_list.append(csv)

        return lead_list
