from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField('Nome do projeto',max_length=64)
    descricao = models.CharField('Descrição', max_length=128, blank=True, null=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Fase(models.Model):
    nome = models.CharField('Nome da fase', max_length=64)
    descricao = models.CharField('Descrição', max_length=128, blank=True, null=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class Tarefa(models.Model):
    nome = models.CharField('Nome da fase', max_length=64)
    descricao = models.CharField('Descrição', max_length=128, blank=True, null=True)
    estado = models.CharField('Estado', max_length=1, blank=True, null=True)
    concluido = models.BooleanField('Concluido', default=False)
    prazo = models.DateField('Prazo')
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

