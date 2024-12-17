from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landingPage'),  # A raiz do app 'landing' exibe a página inicial
    path('logar/', views.login_view, name="logar")
]
