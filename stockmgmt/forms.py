from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['nome_relatorio', 'tipo_relatorio', 'descricao', 'link', 'sob_supervisao']

   def clean_bebida(self):
       nome_relatorio = self.cleaned_data.get('nome_relatorio')
       if not nome_relatorio:
           raise forms.ValidationError( 'Esse campo é obrigatório')

       for instance in Stock.objects.all():
           if instance.nome_relatorio == nome_relatorio:
               raise forms.ValidationError( str( nome_relatorio ) + ' já está cadastrada')
       return nome_relatorio


   def clean_quantidade(self):
       descricao = self.cleaned_data.get( 'descricao' )
       if not descricao:
           raise forms.ValidationError( 'Esse campo é obrigatório' )
       return descricao


class StockSearchForm(forms.ModelForm):
   export_to_CSV = forms.BooleanField(required=False)
   class Meta:
     model = Stock
     fields = ['nome_relatorio']


class StockUpdateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['nome_relatorio', 'tipo_relatorio', 'descricao', 'link', 'sob_supervisao']


# class IssueForm( forms.ModelForm ):
# 	class Meta:
# 		model = Stock
# 		fields = ['reportar_erro', 'erro_por']


# class ReceiveForm( forms.ModelForm ):
# 	class Meta:
# 		model = Stock
# 		fields = ['recebido', 'recebido_por']


# class ReorderLevelForm(forms.ModelForm):
# 	class Meta:
# 		model = Stock
# 		fields = ['reorder_level']




