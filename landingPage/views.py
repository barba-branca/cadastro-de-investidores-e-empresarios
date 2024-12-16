from django.shortcuts import render

def landing_page(request):
    return render(request, 'index.html')  # Refere-se ao template diretamente dentro de 'templates'

def login_view(request):
    return render(request, 'logar.html')  # renderiza sua página de login
