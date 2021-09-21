from django.contrib import admin
from .forms import StockCreateForm

# Register your models here.
from .models import *


class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['nome_relatorio','tipo_relatorio', 'descricao', 'link', 'sob_supervisao']
   form = StockCreateForm
   list_filter = ['nome_relatorio', 'tipo_relatorio', 'descricao']
   search_fields = ['nome_relatorio']

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Tipo_relatorio)
