from django.forms import ModelForm
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

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class Item_pedidoForm(ModelForm):
    class Meta:
        model = Item_pedido
        fields = '__all__'