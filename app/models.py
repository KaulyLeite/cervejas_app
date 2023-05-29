from django.db import models


# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images')
