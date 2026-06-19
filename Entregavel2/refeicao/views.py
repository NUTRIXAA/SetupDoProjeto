from django.shortcuts import render

def home(request):
    return render(request, 'refeicao/index.html')

def login(request):
    return render(request, 'refeicao/login.html')

def cadastro(request):
    return render(request, 'refeicao/cadastro.html')

def planejamento(request):
    return render(request, 'refeicao/planejamento.html')

def detalhes(request):
    return render(request, 'refeicao/detalhes.html')

def cadastro_refeicao(request):
    return render(request, 'refeicao/cadastro_refeicao.html')

def compras(request):
    return render(request, 'refeicao/compras.html')

def perfil(request):
    return render(request, 'refeicao/perfil.html')