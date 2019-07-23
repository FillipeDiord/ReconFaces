from django.forms import ModelForm
from .models import Pessoa, Contagem

class PersonForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'idade', 'email', 'celular', 'foto1', 'foto2', 'foto3', 'foto4', 'foto5', 'foto6']
