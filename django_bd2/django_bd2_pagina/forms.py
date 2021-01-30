from django import forms
from .models import Jogadores
from .models import Equipas
from .models import Clube
from .models import AcoesDisciplinares
from .models import Campeonatos

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

    
class ClubeForm(forms.ModelForm):
    
    class Meta:
        model = Clube
        fields = ('nome','endereco','telefone','presidente','distrito', 'email')


class AcaoDisciplinarForm(forms.ModelForm):
    
    class Meta:
        model = AcoesDisciplinares
        fields = ('id_tipo_acao_disciplinar','comentario','tempo_jogo')
               
class CampeonatoForm(forms.ModelForm):
    
    class Meta:
        model = Campeonatos
        fields = ('id_modalidade','id_epoca','nome_campeonato')



             
#para em vez de aparecer -------, aparecer select
#   def __init__(self, *args, **kwargs):
#       super(JogadorForm,self).__init__(*args, **kwargs)
#       self.fields['cargo'].empty_label = "Select"
#       #para o código de empregado não ser de preenchimento obrigatório
#       self.fields['emp_codigo'].required = False
