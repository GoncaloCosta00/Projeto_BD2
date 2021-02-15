from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('create/jogador', views.create_jogador, name='create_jogador'),
    path('create/clube', views.create_clube, name='create_clube'),
    path('create/equipa', views.create_equipa, name='create_equipa'),
    path('create/acao_discip', views.create_acao_disciplinar, name='create_acao_discip'),
    path('create/campeonatos', views.create_campeonato, name='create_campeonato'),
    path('create/campeonatos_jogos_jquipas', views.create_campeonatos_jogos_jquipas, name='create_campeonato'),
    path('create/epoca', views.create_epoca, name='create_epoca'),
    path('create/jogos', views.create_jogo, name = 'create_jogo'),
    path('create/modalidades', views.create_modalidade, name = 'create_modalidade'),
    path('create/pontuacoes', views.create_pontuacao, name='create_pontuacao'),
    path('create/substituicoes', views.create_subctituicao, name = 'create_substituicao'),
    path('create/tipos_acao_disciplinar', views.create_tipos_acao_disciplinar, name = 'create_tipos_acao_disciplinar'),
    path('create/tipos_de_pontuacao', views.create_tipos_de_pontuacao, name = 'create_tipos_de_pontuacao'),
    path('create/pontuacoes_jogadores_jogos', views.create_pontuacoes_jogadores_jogos, name = 'create_pontuacoes_jogadores_jogos'),
    path('create/jogos_jogadores_acoesdiscip', views.create_jogos_jogadores_acoesdiscip, name = 'create_jogos_jogadores_acoesdiscip'),
    path('create/jogam', views.create_jogam, name = 'create_jogam'),
    path('create/jogador_jogos_equipa', views.create_jogador_jogos_equipa, name = 'create_jogador_jogos_equipa'),
    path('list', views.jogador_list, name='jogador_list'),
    path('update',views.update ,name='index'),
    path('delete',views.delete ,name='index')
    
]
