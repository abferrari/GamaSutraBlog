# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str
from django.http import HttpResponse

from main.models import Lead
from main.forms import LeadForm
from main.ip_utils import get_client_ip
from blog.settings import BASE_DIR

# Create your views here.
def main(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('thanks') + '?name=' + lead.first_name)

    return render(request, 'main/main.html', context)

def thanks(request):

    context = {'name': ''}

    if 'name' in request.GET:
        context['name'] = request.GET['name']

    return render(request, 'main/thanks.html', context)

# Create your views here.
def downloads_drop(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('thanks') + '?name=' + lead.first_name)

    return render(request, 'main/downloads_drop.html', context)
   

# Create your views here.
def whatsapp4business(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('thanks') + '?name=' + lead.first_name)

    return render(request, 'main/whatsapp-para-empresas.html', context)
  
# Create your views here.
def fivereasons(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('thanks') + '?name=' + lead.first_name)

    return render(request, 'main/cinco-motivos-para-apostar-em-um-app.html', context)

# Create your views here.
def considerations(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('thanks') + '?name=' + lead.first_name)

    return render(request, 'main/o-que-considerar-em-um-app-para-o-seu-negocio.html', context)

# Create your views here.
def havingapp4business(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('thanks') + '?name=' + lead.first_name)

    return render(request, 'main/ter-um-app-para-meu-negocio-e-uma-boa-ideia.html', context)

# Create your views here.
def casenikeadidas(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('thanks') + '?name=' + lead.first_name)

    return render(request, 'main/case-nike-adidas.html', context)

def show(request):
    
    context = {'leads': Lead.list()}

    return render(request, 'main/secret.html', context)


# Create your views here.
def lp_info(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        # PDF download
        file_name = 'uso-de-despositivo-movel-e-usuarios-de-app.pdf'
        path_to_file = BASE_DIR + '/' + 'downloads/' + file_name

        with open(path_to_file, 'r') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=%s' % file_name
            return response
    
        #return redirect(reverse('main'))

    return render(request, 'main/lp-infografico-uso-smartphone.html', context)

# Create your views here.
def lp_caseadidasnike(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        # coisa feia! nao eh assim que se faz!!!
        return render(request, 'main/case-nike-adidas.html')            

    return render(request, 'main/lp-case-adidas-nike.html', context)

def interaction(request):

    lead_form = LeadForm(request.POST or None)

    context = {'lead_form': lead_form}

    if lead_form.is_valid():
        
        lead = lead_form.save(commit=False)
        lead.ip = get_client_ip(request)
        lead.save()

        return redirect(reverse('thanks') + '?name=' + lead.first_name)

    return render(request, 'main/a-interacao-entre-empresa-e-cliente-via-app.html', context)   
