

from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('listar_frequencias/', views.listar_frequencias, name='listar_frequencias'),
    path('frequencia/', views.frequencia, name='frequencia'),
    
    
]