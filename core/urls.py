from django.conf.urls import url, include
from django.urls import path, re_path
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
    lista_item_pedido,
    item_pedido_novo,
    item_pedido_update,
    item_pedido_delete,
)

urlpatterns = [
    re_path(r'^$', home, name='core_home'),

    re_path(r'^funcionarios/', lista_funcionarios, name='core_lista_funcionarios'),
    re_path(r'^funcionario-novo/$', funcionario_novo, name='core_funcionario_novo'),
    re_path(r'^funcionario-update/(?P<id>\d+)/$', funcionario_update, name='core_funcionario_update'),
    re_path(r'^funcionario-delete/(?P<id>\d+)/$', funcionario_delete, name='core_funcionario_delete'),

    re_path(r'^clientes$', lista_clientes, name='core_lista_clientes'),
    re_path(r'^cliente-novo$', cliente_novo, name='core_cliente_novo'),
    re_path(r'^cliente-update(?P<id>\d+)/$', cliente_update, name='core_cliente_update'),
    re_path(r'^cliente-delete/(?P<id>\d+)/$', cliente_delete, name='core_cliente_delete'),

    re_path(r'^fornecedores$', lista_fornecedores, name='core_lista_fornecedores'),
    re_path(r'^fornecedor-novo$', fornecedor_novo, name='core_fornecedor_novo'),
    re_path(r'^fornecedor-update(?P<id>\d+)/$', fornecedor_update, name='core_fornecedor_update'),
    re_path(r'^fornecedor-delete/(?P<id>\d+)/$', fornecedor_delete, name='core_fornecedor_delete'),

    re_path(r'^produtos$', lista_produtos, name='core_lista_produtos'),
    re_path(r'^produto-novo$', produto_novo, name='core_produto_novo'),
    re_path(r'^produto-update(?P<id>\d+)/$', produto_update, name='core_produto_update'),
    re_path(r'^produto-delete/(?P<id>\d+)/$', produto_delete, name='core_produto_delete'),


    re_path(r'^compras$', lista_compras, name='core_lista_compras'),
    re_path(r'^compra-novo$', compra_novo, name='core_compra_novo'),
    re_path(r'^compra-update(?P<id>\d+)/$', compra_update, name='core_compra_update'),
    re_path(r'^compra-delete/(?P<id>\d+)/$', compra_delete, name='core_compra_delete'),

    re_path(r'^vendas$', lista_vendas, name='core_lista_vendas'),
    re_path(r'^venda-novo$', venda_novo, name='core_venda_novo'),
    re_path(r'^venda-update(?P<id>\d+)/$', venda_update, name='core_venda_update'),
    re_path(r'^venda-delete/(?P<id>\d+)/$', venda_delete, name='core_venda_delete'),

    re_path(r'^item-pedido$', lista_item_pedido, name='core_lista_item_pedido'),
    re_path(r'^item-pedido-novo$', item_pedido_novo, name='core_item_pedido_novo'),
    re_path(r'^item-pedido-update(?P<id>\d+)/$', item_pedido_update, name='core_item_pedido_update'),
    re_path(r'^item-pedido-delete/(?P<id>\d+)/$', item_pedido_delete, name='core_item_pedido_delete'),

    re_path(r'^pedidos$', lista_pedidos, name='core_lista_pedidos'),
    re_path(r'^pedido-novo$', pedido_novo, name='core_pedido_novo'),
    re_path(r'^pedido-update(?P<id>\d+)/$', pedido_update, name='core_pedido_update'),
    re_path(r'^pedido-delete/(?P<id>\d+)/$', pedido_delete, name='core_pedido_delete'),
    
]