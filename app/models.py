from django.db import models


# Create your models here.
class Marca(models.Model):
    objects = models.Manager()
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images')

    def __str__(self):
        return self.nome


class Produto(models.Model):
    objects = models.Manager()
    nome = models.CharField(max_length=45)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    conteudo = models.PositiveIntegerField()
    descricao = models.TextField()
    ibu = models.PositiveIntegerField()
    abv = models.FloatField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='images')
    pedido = models.CharField(max_length=8, default='ABCD0123')
    qtde = models.PositiveIntegerField(default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.nome} {self.marca}'
