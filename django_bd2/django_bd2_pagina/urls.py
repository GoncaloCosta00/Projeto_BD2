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
    path('list', views.jogador_list, name='jogador_list'),
    path('update',views.update ,name='index')
]
