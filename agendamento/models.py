from django.db import models #criador de tabelas padrão
from django.contrib.auth.models import User #Usuario padrão do django

#Tabelas são classes
class Espaco(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE) 
    data = models.DateField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

def __str__(self):
    return f"agendamento de {self.usuario}  em {self.data} no {self.espaco}"               