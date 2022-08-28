"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.decorators import login_required

from miapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index" ),  
    path('acceso/', views.acceso, name = "acceso" ), 
    path('registro/', views.register, name = "registro" ),
    path('login_page/', views.login_page, name = "login_page" ),
    path('salir/', views.loginOut, name = "salir" ),
    path('data/', views.data, name = "data" ),
    path('lista/', views.lista, name = "lista" ),      
    path('dashboard/', views.dashboard, name = "dashboard" ),
    path('alta/', views.opciones, name = "alta" ),       
    path('reportes/', views.reportes, name = "reportes" ),
    path('detalle/<int:id>', views.detalle, name = "detalle" ),
    path('actualizar/', views.actualizar, name = "actualizar" ),
    path('subir/', views.upload, name = "subir_post" ),
    path('articulos/', views.showArticulos, name = "articulos" ), 
    path('feed/', views.feed, name = "feed" ), 
    path('elim_articulo/<int:id>', views.elim_articulo, name = 'elim_articulo'),
    path('profile/<int:id>', views.profile, name = 'mi_perfil'),
    path('perfil/', views.perfil, name = 'perfil'),
    path('publicar/', views.CrearArticulo.as_view(), name = 'publicar'),
]

# path('login/', views.login, name = "login" ),
#configurar para cargar imagenes
if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)