from django.shortcuts import render, redirect
from .models import (
    Funcionario,
    Cliente,
    Fornecedor,
    Produto,
    Compra,
    Venda,
    Pedido,
)

from .forms import (
    FuncionarioForm,
    ClienteForm,
    FornecedorForm,
    ProdutoForm,
    CompraForm,
    VendaForm,
    PedidoForm,
)

def home(request):
    context = {'mensagem': 'Olá mundo'}
    return render(request, 'core/index.html', context)

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    form = FuncionarioForm()
    data = {'funcionarios': funcionarios, 'form': form}
    return render(request, 'core/lista_funcionarios.html', data)

def funcionario_novo(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_funcionarios')

def funcionario_update(request, id):
    data = {}
    funcionario = Funcionario.objects.get(id=id)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    data['funcionario'] = funcionario
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('core_lista_funcionarios')
    else:
        return render(request, 'core/update_funcionario.html', data)

def funcionario_delete(request, id):
    funcionario = Funcionario.objects.get(id=id)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('core_lista_funcionarios')
    else:
        return render (request, 'core/delete_confirm.html', {'obj': funcionario})

def lista_clientes(request):
    form = ClienteForm()
    clientes = Cliente.objects.all()
    data = {'clientes': clientes, 'form': form}
    return render(request, 'core/lista_clientes.html', data)

def cliente_novo(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_clientes')

def cliente_update(request, id):
    data = {}
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    data['cliente'] = cliente
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('core_lista_clientes')
    else:
        return render(request, 'core/update_cliente.html', data)

def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('core_lista_clientes')
    else:
        return render (request, 'core/delete_confirm.html', {'obj': cliente})

def lista_fornecedores(request):
    form = FornecedorForm()
    fornecedores = Fornecedor.objects.all()
    data = {'fornecedores': fornecedores, 'form': form}
    return render(request, 'core/lista_fornecedores.html', data)

def fornecedor_novo(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_fornecedores')

def fornecedor_update(request, id):
    data = {}
    fornecedor = Fornecedor.objects.get(id=id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    data['fornecedor'] = fornecedor
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('core_lista_fornecedores')
    else:
        return render(request, 'core/update_fornecedor.html', data)

def fornecedor_delete(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('core_lista_fornecedores')
    else:
        return render (request, 'core/delete_confirm.html', {'obj': fornecedor})

def lista_produtos(request):
    form = ProdutoForm()
    produtos = Produto.objects.all()
    data = {'produtos': produtos, 'form': form}
    return render(request, 'core/lista_produtos.html', data)

def produto_novo(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_produtos')

def produto_update(request, id):
    data = {}
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    data['produto'] = produto
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('core_lista_produtos')
    else:
        return render(request, 'core/update_produto.html', data)

def produto_delete(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('core_lista_produtos')
    else:
        return render (request, 'core/delete_confirm.html', {'obj': produto})

def lista_compras(request):
    form = CompraForm()
    compras = Compra.objects.all()
    data = {'compras': compras, 'form': form}
    return render(request, 'core/lista_compras.html', data)

def compra_novo(request):
    form = CompraForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_compras')

def compra_update(request, id):
    data = {}
    compra = Compra.objects.get(id=id)
    form = CompraForm(request.POST or None, instance=compra)
    data['compra'] = compra
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('core_lista_compras')
    else:
        return render(request, 'core/update_compra.html', data)

def compra_delete(request, id):
    compra = Compra.objects.get(id=id)
    if request.method == 'POST':
        compra.delete()
        return redirect('core_lista_compras')
    else:
        return render (request, 'core/delete_confirm.html', {'obj': compra})

def lista_vendas(request):
    form = VendaForm()
    vendas = Venda.objects.all()
    data = {'vendas': vendas, 'form': form}
    return render(request, 'core/lista_vendas.html', data)

def venda_novo(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_vendas')

def venda_update(request, id):
    data = {}
    venda = Venda.objects.get(id=id)
    form = VendaForm(request.POST or None, instance=venda)
    data['venda'] = venda
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('core_lista_vendas')
    else:
        return render(request, 'core/update_venda.html', data)

def venda_delete(request, id):
    venda = Venda.objects.get(id=id)
    if request.method == 'POST':
        venda.delete()
        return redirect('core_lista_vendas')
    else:
        return render (request, 'core/delete_confirm.html', {'obj': venda})

def lista_pedidos(request):
    form = PedidoForm()
    pedidos = Pedido.objects.all()
    data = {'pedidos': pedidos, 'form': form}
    return render(request, 'core/lista_pedidos.html', data)

def pedido_novo(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pedidos')

def pedido_update(request, id):
    data = {}
    pedido = Pedido.objects.get(id=id)
    form = PedidoForm(request.POST or None, instance=pedido)
    data['pedido'] = pedido
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('core_lista_pedidos')
    else:
        return render(request, 'core/update_pedido.html', data)

def pedido_delete(request, id):
    pedido = Pedido.objects.get(id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('core_lista_pedidos')
    else:
        return render (request, 'core/delete_confirm.html', {'obj': pedido})
