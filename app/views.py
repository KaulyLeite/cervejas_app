from app.models import Marca, Produto
from datetime import datetime
from django.shortcuts import render
import uuid

TEMPLATE_BASE = 'main/base.html'
TEMPLATE_PRODUTOS = 'main/produtos.html'
TEMPLATE_SOBRE = 'main/sobre.html'
TEMPLATE_PEDIDOS = 'main/pedidos.html'
TEMPLATE_CONFIRMACAO = 'main/confirmacao.html'
TEMPLATE_ENVIO = 'main/envio.html'


# Create your views here.
def index(request):
    marcas = Marca.objects.all()
    return render(request, TEMPLATE_BASE, {'marcas': marcas})


def produtos(request):
    produtos_listados = Produto.objects.all()
    return render(request, TEMPLATE_PRODUTOS, {'produtos': produtos_listados})


def sobre(request):
    return render(request, TEMPLATE_SOBRE)


def pedidos(request):
    produtos_pedidos = Produto.objects.all()
    return render(request, TEMPLATE_PEDIDOS, {'produtos': produtos_pedidos})


def confirmacao(request):
    produtos_confirmados = Produto.objects.all()
    if request.method == 'POST':
        pedido = uuid.uuid4().hex[:8].upper()

        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        estado = request.POST['estado']

        data = datetime.now().strftime('%d/%m/%Y')

        produtos_selecionados = []
        for produto in produtos_confirmados:
            qtde_key = f'{produto.id}_qtde'
            qtde = int(request.POST.get(qtde_key, 0))
            if qtde > 0:
                produto.total = produto.valor * qtde
                produto.qtde = qtde
                produto.pedido = pedido
                produto.save()
                produtos_selecionados.append(produto)

        total_pedido = sum(produto.total for produto in produtos_selecionados)

        return render(request, TEMPLATE_CONFIRMACAO,
                      {'pedido': pedido,
                       'nome': nome,
                       'email': email,
                       'telefone': telefone,
                       'endereco': endereco,
                       'cidade': cidade,
                       'estado': estado,
                       'data': data,
                       'produtos': produtos_selecionados,
                       'total_pedido': total_pedido
                       })
    return render(request, TEMPLATE_PEDIDOS, {'produtos': produtos})


def envio(request):
    if request.method == 'POST':
        pedido = request.POST['pedido']
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        data = request.POST['data']
        produtos_selecionados = Produto.objects.filter(pedido=pedido)
        total_pedido = request.POST['total_pedido']

        return render(request, TEMPLATE_ENVIO, {
            'pedido': pedido,
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'endereco': endereco,
            'cidade': cidade,
            'estado': estado,
            'data': data,
            'produtos': produtos_selecionados,
            'total_pedido': total_pedido
        })
