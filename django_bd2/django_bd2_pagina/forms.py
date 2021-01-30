from django import forms
from .models import Jogadores
from .models import Equipas

class JogadorForm(forms.ModelForm):

    class Meta:
        model = Jogadores
        fields = ('nome','data_nascimento','telemovel','altura','naturalidade')
        labels = {
            'nome':'Nome Completo','data_nascimento':'Data de Nascimento','telemovel':'Telemóvel','altura':'Altura', 'naturalidade':'Naturalidade'
        }

class EquipaForm(forms.ModelForm):
    
    class Meta:
        model = Equipas
        fields = ('id_genero','id_clube','id_modalidade','id_faixa_etaria','equipa', 'treinador', 'sede', 'telefone', 'email')
               
#para em vez de aparecer -------, aparecer select
#   def __init__(self, *args, **kwargs):
#       super(JogadorForm,self).__init__(*args, **kwargs)
#       self.fields['cargo'].empty_label = "Select"
#       #para o código de empregado não ser de preenchimento obrigatório
#       self.fields['emp_codigo'].required = False
