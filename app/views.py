from app.models import Marca, Produto
from datetime import datetime
from django.conf import settings
from django.shortcuts import render
import configparser
import email as emailpkg
import locale
import logging
import os
import smtplib
import uuid

APP_NAME = settings.APP_NAME
APP_VERSION = settings.APP_VERSION
LOGGER = logging.getLogger(__name__)
TEMPLATE_BASE = 'main/base.html'
TEMPLATE_PRODUTOS = 'main/produtos.html'
TEMPLATE_SOBRE = 'main/sobre.html'
TEMPLATE_PEDIDOS = 'main/pedidos.html'
TEMPLATE_CONFIRMACAO = 'main/confirmacao.html'
TEMPLATE_ENVIO = 'main/envio.html'


# Create your views here.
def index(request):
    marcas = Marca.objects.all()

    nomes_marcas = [marca.nome for marca in marcas]

    if nomes_marcas:
        num_marcas = len(nomes_marcas)
        if num_marcas > 1:
            ultima_marca = nomes_marcas.pop()
            nomes_marcas = ', '.join(nomes_marcas)
            nomes_marcas += f' e {ultima_marca}'
        else:
            nomes_marcas = nomes_marcas[0]
    else:
        nomes_marcas = ""

    titulo = f"A Carlos Cervejas Especiais é distribuidora exclusiva das cervejas {nomes_marcas}" \
             f" em toda a região de Garopaba e Imbituba - Santa Catarina."

    return render(request, TEMPLATE_BASE, {
        'name': APP_NAME,
        'version': APP_VERSION,
        'marcas': marcas,
        'titulo': titulo
    })


def produtos(request):
    produtos_listados = Produto.objects.all()

    return render(request, TEMPLATE_PRODUTOS, {
        'name': APP_NAME,
        'version': APP_VERSION,
        'produtos': produtos_listados
    })


def sobre(request):
    config = configparser.ConfigParser()
    config.read('config.ini')

    if 'SOBRE' in config:
        email = config['SOBRE'].get('email')
        telefone = config['SOBRE'].get('telefone')
        whatsapp = config['SOBRE'].get('whatsapp')
    else:
        email = ''
        telefone = ''
        whatsapp = ''

    return render(request, TEMPLATE_SOBRE, {
        'name': APP_NAME,
        'version': APP_VERSION,
        'email': email,
        'telefone': telefone,
        'whatsapp': whatsapp
    })


def pedidos(request):
    produtos_pedidos = Produto.objects.all()

    return render(request, TEMPLATE_PEDIDOS, {
        'name': APP_NAME,
        'version': APP_VERSION,
        'produtos': produtos_pedidos
    })


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

        return render(request, TEMPLATE_CONFIRMACAO, {
            'name': APP_NAME,
            'version': APP_VERSION,
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
    return render(request, TEMPLATE_PEDIDOS, {
        'name': APP_NAME,
        'version': APP_VERSION,
        'produtos': produtos
    })


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

        try:
            envio_email(pedido, nome, email, telefone, endereco,
                        cidade, estado, data_hora, produtos_selecionados, total_pedido)
        except Exception as e:
            erro_descricao = str(e)
            LOGGER.error('Ocorreu um erro ao enviar o pedido: %s', erro_descricao)
            return render(request, TEMPLATE_ENVIO, {
                'name': APP_NAME,
                'version': APP_VERSION,
                'pedido': pedido,
                'erro_envio': True,
                'erro_descricao': erro_descricao
            })

        return render(request, TEMPLATE_ENVIO, {
            'name': APP_NAME,
            'version': APP_VERSION,
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

        descricao += f'Produto: {produto.nome} {produto.marca}<br>'
        descricao += f'Valor unitário: R$ {valor_formatado}<br>'
        descricao += f'Quantidade: {produto.qtde}<br>'
        descricao += f'Valor total: R$ {total_formatado}<br>'
        descricao += '<br>'

    descricao += f'Valor total do pedido: R$ {total_pedido}<br>'

    mensagem = emailpkg.message.Message()
    mensagem['Subject'] = f'Pedido: {pedido} - Carlos Cervejas Especiais'

    config = configparser.ConfigParser()
    config.read('config.ini')
    remetente = os.getenv('EMAIL_REMETENTE', '')
    senha = os.getenv('EMAIL_SENHA', '')
    destinatarios = [remetente, email]

    mensagem['From'] = remetente
    mensagem['To'] = ', '.join(destinatarios)

    mensagem.add_header('Content-Type', 'text/html')
    mensagem.set_payload(descricao)

    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(remetente, senha)
    smtp.sendmail(remetente, destinatarios, mensagem.as_string().encode('utf-8'))
    smtp.quit()
