from django.shortcuts import render
from app_cadastro.models import usuarios


def index(request):
    return render(request, "cadastros/pages/index.html")

def usuarios_page(request):
    novo_usuario = usuarios()

    # criando uma novo usuario
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')

    #salvando os dados da tema no banco de dados
    novo_usuario.save()

    # exibir todos os usuarios ja cadastrados no banco de dados
    # o django espera esta dentro de um dicionario
    todos_os_usuarios = {
        'todos_os_usuarios': usuarios.objects.all()
    }

    # retornar os dados para a pagina de usuarios
    return render(request, "cadastros/pages/usuarios.html", todos_os_usuarios)


