from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    lista_fornece = models.CharField(max_length=30)
class Categoria(models.Model):
    lista_ctg = models.CharField(max_length=50)
    def __str__(self):
        return self.lista_ctg
class Estoque(models.Model):
    lista_produto = models.CharField(max_length=20)
    cod_produto = models.CharField( max_length=15, unique=True)
    desc_produto = models.CharField( max_length=100)
    preco_produto = models.DecimalField( max_digits=5, decimal_places=2)
    data_pro = models.DateField( auto_now=False, auto_now_add=False)
    ctg = models.ManyToManyField(Categoria, related_name='produtos')
    fornece = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    def __str__(self):
        return self.lista_produto
    
    def __str__(self):
        return self.lista_produto
    