from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST": 
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')


        if senha != confirmar_senha:
            print(1)
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            print(2)
            return redirect('/usuarios/cadastro')

        user = User.objects.create_user(
            username=username,
            password=senha
        )
            
        return redirect('/usuarios/logar') #vai dar erro, url nao existe
            


        return HttpResponse(f'{username} - {senha} - {confirmar_senha}')