from main.models import Lead
from django.utils.timezone import localtime
from maintenance.report import report

def do():
    aaa = Lead.objects.all()
    for a in aaa:
        print '%s %s %s %s %s' % (
            a.id,
            a.first_name, 
            a.last_name, 
            localtime(a.timestamp), a.ip)


def reset():
    Lead.objects.all().delete()
    
def time():
    from django.utils import timezone
    print timezone.now()
    print localtime(timezone.now())
