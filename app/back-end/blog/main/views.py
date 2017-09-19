# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from main.forms import LeadForm
from main.ip_utils import get_client_ip

# Create your views here.
def main(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('main'))

    return render(request, 'main/main.html', context)

def thanks(request):
    return render(request, 'main/thanks.html')

# Create your views here.
def downloads_drop(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('main'))

    return render(request, 'main/downloads_drop.html', context)
   

# Create your views here.
def whatsapp4business(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('main'))

    return render(request, 'main/whatsapp-para-empresas.html', context)
  
# Create your views here.
def fivereasons(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('main'))

    return render(request, 'main/cinco-motivos-para-apostar-em-um-app.html', context)

# Create your views here.
def considerations(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('main'))

    return render(request, 'main/o-que-considerar-em-um-app-para-o-seu-negocio.html', context)

