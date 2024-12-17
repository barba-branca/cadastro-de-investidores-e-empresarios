from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('landingPage.urls')),  # A raiz do site agora vai para a landing page
    path('admin/', admin.site.urls),  # Rota para o painel de administração do Django
    path('usuarios/', include('usuarios.urls')),  # Inclui as URLs do app 'usuarios'
    path('empresarios/', include('empresarios.urls')),  # Rota para o app 'empresarios'
    path('investidores/', include('investidores.urls')),  # Rota para o app 'investidores'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve arquivos de mídia em desenvolvimento
