from django.db import models


class Diretor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    nacionalidade = models.CharField(max_length=60, blank=True)

    class Meta:
        verbose_name = "diretor"
        verbose_name_plural = "diretores"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField("título", max_length=150)
    ano_lancamento = models.PositiveIntegerField("ano de lançamento")
    nota = models.DecimalField(max_digits=3, decimal_places=1, help_text="Nota de 0 a 10")
    sinopse = models.TextField(blank=True)
    diretor = models.ForeignKey(Diretor, on_delete=models.PROTECT, related_name="filmes")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="filmes")

    class Meta:
        verbose_name = "filme"
        verbose_name_plural = "filmes"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
