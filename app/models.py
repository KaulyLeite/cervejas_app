from django.db import models


# Create your models here.
class Marca(models.Model):
    objects = models.Manager()
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images')


class Produto(models.Model):
    objects = models.Manager()
    nome = models.CharField(max_length=45)
    conteudo = models.PositiveIntegerField()
    descricao = models.TextField()
    ibu = models.PositiveIntegerField()
    abv = models.FloatField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='images')
    pedido = models.CharField(max_length=8, default='ABCD0123')
    qtde = models.PositiveIntegerField(default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
