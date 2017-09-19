import codecs
from main.models import Lead
from django.utils.timezone import localtime


def report():
    
    file_handler = codecs.open('leads.csv', 'w', 'utf8') 

    header = 'email,nome,ip,tipo,data_hora'
    
    file_handler.write(header + '\n')

    for lead in Lead.list():
        file_handler.write(lead + '\n')

    print 'Done'
    file_handler.close()
