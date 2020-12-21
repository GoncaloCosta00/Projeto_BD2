from django.urls import path
from . import views //import da view a usar
urlpatterns = [
    path('', views.index, name='index'), //configuração do caminho e parte da view a usar
]
