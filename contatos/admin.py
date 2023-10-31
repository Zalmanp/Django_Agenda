from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome', 'telefone','email','data_nascimento','entrada_staff','categoria', 'mostrar')
    list_display_links = ('id','nome','sobrenome')
    search_fields = ('nome', 'sobrenome', 'telefone')
    #list_filter = ('nome','sobrenome')
    list_per_page = 10
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)