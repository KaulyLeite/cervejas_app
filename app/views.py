from django.shortcuts import render

from app.models import Marca, Produto

TEMPLATE_BASE = "main/base.html"
TEMPLATE_PRODUTOS = "main/produtos.html"
TEMPLATE_SOBRE = "main/sobre.html"
TEMPLATE_PEDIDOS = "main/pedidos.html"


# Create your views here.
def index(request):
    marcas = Marca.objects.all()
    return render(request, TEMPLATE_BASE, {'marcas': marcas})


def produtos(request):
    produtos = Produto.objects.all()
    return render(request, TEMPLATE_PRODUTOS, {'produtos': produtos})


def sobre(request):
    return render(request, TEMPLATE_SOBRE)


def pedidos(request):
    produtos = Produto.objects.all()
    return render(request, TEMPLATE_PEDIDOS, {'produtos': produtos})
