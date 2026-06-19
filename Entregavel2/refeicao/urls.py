from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('planejamento/', views.planejamento, name='planejamento'),
    path('detalhes/', views.detalhes, name='detalhes'),
    path('cadastro-refeicao/', views.cadastro_refeicao, name='cadastro_refeicao'),
    path('compras/', views.compras, name='compras'),
    path('perfil/', views.perfil, name='perfil'),
]