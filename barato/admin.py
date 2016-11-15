from django.contrib import admin
from .models import Fornecedor, Produto, Marca
# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Marca)