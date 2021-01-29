from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('list', views.list, name='index'),
    path('update',views.update ,name='index')
]
