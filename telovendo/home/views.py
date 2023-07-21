from django.shortcuts import render
from .models import Usuario



# Create your views here.

def bienvenida(request):
    return render(request, 'home/index.html', {
        } )

def mostrarUsuario(request):
    lista_usuario = Usuario.objects.all()
    return render(request, 'home/mostrar_usuario.html', {
        'lista_usuario' : lista_usuario
    })