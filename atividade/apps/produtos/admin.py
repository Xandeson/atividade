from django.contrib import admin
from .models import Estoque, Fornecedor, Categoria
# Register your models here.


admin.site.register(Estoque)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
