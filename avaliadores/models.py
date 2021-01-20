from django.db import models
from django.contrib.auth.models import User

class Avaliadores(models.Model):
    nome = models.CharField(max_length=80, verbose_name='Nome')
  #  perfil = models.ForeignKey(User, on_delete=models.PROTECT) # toda avaliador precisa de um loggin #
    cnpj = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome', ]

    def __str__(self):
        return self.nome


