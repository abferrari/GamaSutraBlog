from django.forms import ModelForm
from main.models import Lead

class LeadForm(ModelForm):

    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'email']

        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'e-mail',
        }

