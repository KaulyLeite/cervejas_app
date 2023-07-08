from app.models import Marca, Produto
from datetime import datetime
from django.conf import settings
from django.shortcuts import render
import configparser
import email as emailpkg
import locale
import smtplib
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
    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config['SOBRE']['email']
    telefone = config['SOBRE']['telefone']
    whatsapp = config['SOBRE']['whatsapp']

    return render(request, TEMPLATE_SOBRE,
                  {'email': email,
                   'telefone': telefone,
                   'whatsapp': whatsapp
                   })


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

        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

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
                       'data_hora': data_hora,
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
        data_hora = request.POST['data_hora']
        produtos_selecionados = Produto.objects.filter(pedido=pedido)
        total_pedido = request.POST['total_pedido']

        envio_email(pedido, nome, email, telefone, endereco,
                    cidade, estado, data_hora, produtos_selecionados, total_pedido)

        return render(request, TEMPLATE_ENVIO, {
            'pedido': pedido,
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'endereco': endereco,
            'cidade': cidade,
            'estado': estado,
            'data_hora': data_hora,
            'produtos': produtos_selecionados,
            'total_pedido': total_pedido
        })


def envio_email(pedido, nome, email, telefone, endereco,
                cidade, estado, data_hora, produtos_selecionados, total_pedido):
    language_code = settings.LANGUAGE_CODE
    locale.setlocale(locale.LC_ALL, language_code)

    descricao = 'Obrigado por realizar o seu pedido conosco!<br>'
    descricao += 'Em breve entraremos em contato neste e-mail para mais ' \
                 'detalhes sobre o pagamento e entrega do pedido.<br>'
    descricao += '<br>'
    descricao += 'Dados do pedido:<br>'
    descricao += '<br>'
    descricao += f'Pedido: {pedido}<br>'
    descricao += f'Nome: {nome}<br>'
    descricao += f'E-mail: {email}<br>'
    descricao += f'Telefone: {telefone}<br>'
    descricao += f'Endereço: {endereco}<br>'
    descricao += f'Cidade, Estado: {cidade}, {estado}<br>'
    descricao += f'Data e Hora: {data_hora}<br>'
    descricao += '<br>'

    for produto in produtos_selecionados:
        valor_formatado = locale.currency(produto.valor, grouping=True, symbol=True)
        total_formatado = locale.currency(produto.total, grouping=True, symbol=True)

        descricao += f'Produto: {produto.nome}<br>'
        descricao += f'Valor unitário: R$ {valor_formatado}<br>'
        descricao += f'Quantidade: {produto.qtde}<br>'
        descricao += f'Valor total: R$ {total_formatado}<br>'
        descricao += '<br>'

    descricao += f'Valor total do pedido: R$ {total_pedido}<br>'

    mensagem = emailpkg.message.Message()
    mensagem['Subject'] = f'Pedido: {pedido} - Carlos Cervejas Especiais'

    config = configparser.ConfigParser()
    config.read('config.ini')
    remetente = config['EMAIL']['remetente']
    destinatarios = [remetente, email]
    senha = config['EMAIL']['senha']

    mensagem['From'] = remetente
    mensagem['To'] = ', '.join(destinatarios)

    mensagem.add_header('Content-Type', 'text/html')
    mensagem.set_payload(descricao)

    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(remetente, senha)
    smtp.sendmail(remetente, destinatarios, mensagem.as_string().encode('utf-8'))
    smtp.quit()
