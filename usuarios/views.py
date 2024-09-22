from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST": 
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')


        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha precisa ter pelo menos 6 digitos')
            return redirect('/usuarios/cadastro')

        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuario com esse username')
            return redirect('/usuarios/cadastro')
       
        user = User.objects.create_user(
            username=username,
            password=senha
        )
            
        return redirect('/usuarios/logar') #vai dar erro, url nao existe
            


        
def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)
        if  user:
            auth.login(request, user)
            return redirect('/empresarios/cadstrar_empresas') # Vai dar erro
        messages.add_message(request, constants.ERROR, 'Usuario ou senha invalida')
        return redirect('/usuarios/logar')