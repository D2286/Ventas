from django.shortcuts import render
from Modulos.miregistro.models import Pedido, Cliente


def Plantillauno(request):
    data = {
        'name': 'Diego',
        'Compra': Pedido.objects.all()
    }
    return render(request, 'Plantilla.html', data)

def Plantillados(request):
    data = {
        'name': 'Diego',
        'Nombre': Cliente.objects.all()
    }
    return render(request, 'Second.html', data)