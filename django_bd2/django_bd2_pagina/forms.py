from django import forms
from .models import AcoesDisciplinares, Campeonatos, CampeonatosJogosEquipas, Clube, Epocas, Equipas, Jogadores, JogadoresJogosEquipas, Jogam, Jogos, JogosJogadoresAcoesdiscip, Modalidades, Pontuacoes, PontuacoesJogadoresJogos, Substituicoes, TipoAcaoDisciplinar, TipoPontuacao




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


class CampeonatoJogosEquipasForm(forms.ModelForm):
    
    class Meta:
        model = CampeonatosJogosEquipas
        fields = ('id_jogo','id_campeonato','id_equipa')

class EpocaForm(forms.ModelForm):

     class Meta:
        model = Epocas
        fields = ('ano_inicio','ano_fim')

class Jogador_jogos_equipaForm(forms.ModelForm):

     class Meta:
        model = JogadoresJogosEquipas
        fields = ('id_equipa','id_jogo','id_jogador','titular','numero_jogador')


class JogamForm(forms.ModelForm):

     class Meta:
        model = Jogam
        fields = ('id_jogador','id_equipa')

class JogosForm(forms.ModelForm):

     class Meta:
        model = Jogos
        fields = ('data_hora','local')

class Jogos_jogadores_acoesdiscipForm(forms.ModelForm):

     class Meta:
        model = JogosJogadoresAcoesdiscip
        fields = ('id_jogo','id_jogador','id_acao_disciplinar')

class ModalidadesForm(forms.ModelForm):

     class Meta:
        model = Modalidades
        fields = ('modalidade',)

class PontuacoesForms(forms.ModelForm):

     class Meta:
        model = Pontuacoes
        fields = ('id_tipo_pontuacao','pontuacao','tempo_jogo')

class Pontuacoes_jogadores_jogosForm(forms.ModelForm):

     class Meta:
        model = PontuacoesJogadoresJogos
        fields = ('id_pontuacao','id_jogador','id_jogo')

class SubstituicoesForm(forms.ModelForm):

     class Meta:
        model = Substituicoes
        fields = ('id_jogador','id_jogo','tempo_jogo','entra','sai')

class Tipos_acao_disciplinarForm(forms.ModelForm):

     class Meta:
        model = TipoAcaoDisciplinar
        fields = ('acao_disciplinar',)

class Tipos_de_pontuacaoForm(forms.ModelForm):

     class Meta:
        model = TipoPontuacao
        fields = ('tipo_pontuacao',)




             
#para em vez de aparecer -------, aparecer select
#   def __init__(self, *args, **kwargs):
#       super(JogadorForm,self).__init__(*args, **kwargs)
#       self.fields['cargo'].empty_label = "Select"
#       #para o código de empregado não ser de preenchimento obrigatório
#       self.fields['emp_codigo'].required = False
