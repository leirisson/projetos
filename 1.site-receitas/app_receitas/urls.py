from django.urls import path

from app_receitas.views import index


# arquivo index do projeto
urlpatterns = [
    path("", index)
]
