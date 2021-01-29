from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create),
    path('list', views.list, name='index'),
    path('update',views.update ,name='index')
]
