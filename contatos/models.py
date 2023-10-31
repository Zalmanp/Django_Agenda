from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    Ja_saiu_da_staff = 1
    Saiu_mais_de_1x = 2
    Permaneceu = 3
    SAIDA_ENTRADA = (
        (Ja_saiu_da_staff, '1x'),
        (Saiu_mais_de_1x, '>2x'),
        (Permaneceu, 'Perma'),
    )
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cpf = models.CharField(max_length=255)
    Saida_staff = models.PositiveSmallIntegerField(choices=SAIDA_ENTRADA, blank=True, null=True)
    entrada_staff = models.DateTimeField(default=timezone.now)
    data_nascimento = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')
    identidade_front = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')
    identidade_back = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome
