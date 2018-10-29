from django.conf.urls import url, include
from django.urls import path
from .views import (
    home,
    lista_clientes,
    lista_funcionarios,
    lista_fornecedores,
    lista_produtos,
    lista_pedidos,
    lista_compras,
    lista_vendas,
    funcionario_novo,
    cliente_novo,
    fornecedor_novo,
    produto_novo,
    compra_novo,
    venda_novo,
    pedido_novo,
    funcionario_update,
    cliente_update,
    fornecedor_update,
    produto_update,
    compra_update,
    venda_update,
    pedido_update,
    funcionario_delete,
    cliente_delete,
    fornecedor_delete,
    produto_delete,
    compra_delete,
    venda_delete,
    pedido_delete,
)

urlpatterns = [
    path('', home, name='core_home'),

    path('funcionarios/', lista_funcionarios, name='core_lista_funcionarios'),
    path('funcionario-novo/', funcionario_novo, name='core_funcionario_novo'),
    path('funcionario-update/(?P<id>\d+)/$', funcionario_update, name='core_funcionario_update'),
    path('funcionario-delete/(?P<id>\d+)/$', funcionario_delete, name='core_funcionario_delete'),

    path('clientes', lista_clientes, name='core_lista_clientes'),
    path('cliente-novo', cliente_novo, name='core_cliente_novo'),
    path('cliente-update(?P<id>\d+)/$', cliente_update, name='core_cliente_update'),
    path('cliente-delete/(?P<id>\d+)/$', cliente_delete, name='core_cliente_delete'),

    path('fornecedores', lista_fornecedores, name='core_lista_fornecedores'),
    path('fornecedor-novo', fornecedor_novo, name='core_fornecedor_novo'),
    path('fornecedor-update(?P<id>\d+)/$', fornecedor_update, name='core_fornecedor_update'),
    path('fornecedor-delete/(?P<id>\d+)/$', fornecedor_delete, name='core_fornecedor_delete'),

    path('produtos', lista_produtos, name='core_lista_produtos'),
    path('produto-novo', produto_novo, name='core_produto_novo'),
    path('produto-update(?P<id>\d+)/$', produto_update, name='core_produto_update'),
    path('produto-delete/(?P<id>\d+)/$', produto_delete, name='core_produto_delete'),


    path('compras', lista_compras, name='core_lista_compras'),
    path('compra-novo', compra_novo, name='core_compra_novo'),
    path('compra-update(?P<id>\d+)/$', compra_update, name='core_compra_update'),
    path('compra-delete/(?P<id>\d+)/$', compra_delete, name='core_compra_delete'),

    path('vendas', lista_vendas, name='core_lista_vendas'),
    path('venda-novo', venda_novo, name='core_venda_novo'),
    path('venda-update(?P<id>\d+)/$', venda_update, name='core_venda_update'),
    path('venda-delete/(?P<id>\d+)/$', venda_delete, name='core_venda_delete'),

    path('pedidos', lista_pedidos, name='core_lista_pedidos'),
    path('pedido-novo', pedido_novo, name='core_pedido_novo'),
    path('pedido-update(?P<id>\d+)/$', pedido_update, name='core_pedido_update'),
    path('pedido-delete/(?P<id>\d+)/$', pedido_delete, name='core_pedido_delete'),

    
]