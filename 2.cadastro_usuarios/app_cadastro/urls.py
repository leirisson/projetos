from django.urls import path
from app_cadastro.views import index, usuarios_page

urlpatterns = [
    path("", index, name="home"),
    path("usuarios/", usuarios_page, name="listagem_usuarios" ),
]
