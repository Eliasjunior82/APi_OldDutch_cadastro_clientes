from django.contrib import admin
from oldDutch.models import cliente


class Clientes(admin.ModelAdmin):
    list_display = ('id','nome', 'telefone','data')
    list_display_links = ('id', 'nome')
    search_fields= ['nome']
    list_per_page = 15

admin.site.register(cliente, Clientes)
