import codecs
from main.models import Lead
from django.utils.timezone import localtime


def report():
    
    #file_handler = open('leads.csv', 'w+')
    file_handler = codecs.open('leads.csv', 'w', 'utf8') 

    header = 'Nome Completo,e-mail,data,hora,IP'
    
    file_handler.write(header + '\n')

    for lead in Lead.objects.all():
        reg = {
            'full_name': lead.first_name + ' ' + lead.last_name,
            'email': lead.email,
            'date': localtime(lead.timestamp).strftime('%d/%m/%Y'),
            'hour': localtime(lead.timestamp).strftime('%H:%M:%S'),
            'IP': lead.ip,
        }
        csv = '{full_name},{email},{date},{hour},{IP}'.format(**reg)
        file_handler.write(csv + '\n')

    print 'Done'
    file_handler.close()
