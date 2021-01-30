from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('create/jogador', views.create_jogador, name='create_jogador'),
    path('create/equipa', views.create_equipa, name='create_jogador'),
    path('list', views.list, name='index'),
    path('update',views.update ,name='index')
]
