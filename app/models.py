from django.db import models

class Dados(models.Model):
    nome_area = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)	
    estado = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    area_verde = models.DecimalField(decimal_places=2, max_digits=10)
    area_arborizada = models.CharField(max_length=3)
    vegetacao_perturbada = models.CharField(max_length=3)
    vegetacao_conservada = models.CharField(max_length=3)	
    fauna_nativa = models.CharField(max_length=3)
    mitigacao_ilhas_de_calor = models.CharField(max_length=3)


# Create your models here.
