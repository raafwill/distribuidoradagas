from django.db import models



bebida_choice = (
		('Auditoria', 'Brahma'),
		('Skol', 'Skol'),
		('Glacial', 'Glacial'),)

# Create your models here.

class Tipo_relatorio(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Stock(models.Model):

	tipo_relatorio = models.ForeignKey(Tipo_relatorio, on_delete=models.CASCADE, blank=True)
	descricao = models.CharField( max_length=140, blank=True, null=True )
	nome_relatorio = models.CharField(max_length=140, blank=True, null=True)
	link = models.URLField( max_length=50, blank=True, null=True )
	sob_supervisao = models.CharField( max_length=50, blank=True, null=True)
	reportar_erro = models.IntegerField(default='0', blank=False, null=True)
	# data_recebimento = models.DateTimeField(auto_now_add=False, auto_now=True)
	# erro_por = models.CharField( max_length=50, blank=True, null=True )
	# recebido = models.IntegerField(default='0', blank=False, null=True)
	# recebido_por = models.CharField( max_length=50, blank=True, null=True )
	# reorder_level = models.IntegerField(default='0', blank=False, null=True)

	def __str__(self):
		return self.nome_relatorio

