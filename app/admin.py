from django.contrib import admin
from .models import Marca, Produto


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    exclude = ('pedido', 'qtde', 'total')


admin.site.register(Marca)
admin.site.register(Produto, ProdutoAdmin)
