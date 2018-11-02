from django.contrib import admin
from .models import (
    Funcionario,
    Cliente,
    Fornecedor,
    Produto,
    Compra,
    Venda,
    Pedido,
)

class movPedidoAdmin(admin.ModelAdmin):
    list_display = (
        'cliente', 'data_hora', 'valor', 'itens', 'pago')

class movProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'pizza_Sabor',
        'descricao',
        'cod_pizza',
        'valor',
    )

admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Produto, movProdutoAdmin)
admin.site.register(Compra)
admin.site.register(Venda)
admin.site.register(Pedido, movPedidoAdmin)
# Register your models here.
