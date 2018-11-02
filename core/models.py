from django.db import models
import math

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    cargo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=18)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    pizza_Sabor = models.CharField(max_length=100)    
    descricao = models.CharField(max_length=200)
    cod_pizza = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    

    def __str__(self):
        return self.pizza_Sabor

class Compra(models.Model):
    dataCompra = models.DateField(auto_now = False , auto_now_add = False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    produto_compra = models.CharField(max_length=100)
    valorCompra = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.produto_compra

class Venda(models.Model):
    descricao = models.CharField(max_length=200)
    dataVenda = models.DateField(auto_now = False , auto_now_add = False)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    totalVendas = models.DecimalField(max_digits=5, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Pedido(models.Model):
    
    itens = models.TextField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data_hora = models.DateTimeField(auto_now = False , auto_now_add = False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.cliente.nome

