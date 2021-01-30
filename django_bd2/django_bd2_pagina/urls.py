from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('create/jogador', views.create_jogador, name='create_jogador'),
    path('list', views.jogador_list, name='jogador_list'),
    path('update',views.update ,name='index')
]
