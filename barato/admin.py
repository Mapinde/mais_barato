from django.contrib import admin
from .models import Fornecedor, Produto
# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Produto)