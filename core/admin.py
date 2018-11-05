from django.contrib import admin
from .models import (
    Funcionario,
    Cliente,
    Fornecedor,
    Produto,
    Compra,
    Venda,
    Pedido,
    Item_pedido,
)

class movFuncionarioAdmin(admin.ModelAdmin):
    list_display = (
            'nome',
            'endereco',
            'telefone',
            'cpf',
            'cargo',
    )

class movClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'endereco',
        'telefone',
        'cpf',
    )

class movFornecedoradmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'endereco',
        'telefone',
        'cnpj',
    )

class movProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'pizza_Sabor',
        'descricao',
        'codigo_pizza',
        'valor',
    )

class movCompraAdmin(admin.ModelAdmin):
    list_display = (
        'dataCompra',
        'fornecedor',
        'produto_compra',
        'valorCompra',
    )

class movVendaAdmin(admin.ModelAdmin):
    list_display = (
        'descricao',
        'dataVenda',
        'valor',
        'totalVendas',
        'cliente',
    )

class movItemPedidoAdmin(admin.ModelAdmin):
    list_display = (
        'quantidade',
        'produto',
        'cliente',
    )

class movPedidoAdmin(admin.ModelAdmin):
    list_display = (
        'item_pedido',
        'funcionario',
        'data_hora',
        'cliente',
        'produto',
        'pago',
        'totalPedido',
    )

# Register your models here.

admin.site.register(Funcionario, movFuncionarioAdmin)
admin.site.register(Cliente, movClienteAdmin)
admin.site.register(Fornecedor, movFornecedoradmin)
admin.site.register(Produto, movProdutoAdmin)
admin.site.register(Compra, movCompraAdmin)
admin.site.register(Venda, movVendaAdmin)
admin.site.register(Pedido, movPedidoAdmin)
admin.site.register(Item_pedido, movItemPedidoAdmin)
