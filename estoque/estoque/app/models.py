from django.db import models

# Create your models here.

class Estoque(models.Model):
    lista_produto = models.CharField(max_length=20)
    cod_produto = models.models.CharField( max_length=15, unique=True)
    desc_produto = models.models.CharField( max_length=100)
    preco_produto = models.DecimalField( max_digits=5, decimal_places=2)
    data_pro = models.DateField( auto_now=False, auto_now_add=False)
