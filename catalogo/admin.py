from django.contrib import admin

from .models import Categoria, Diretor, Filme


@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ("nome", "nacionalidade")
    search_fields = ("nome",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "diretor", "categoria", "ano_lancamento", "nota")
    list_filter = ("diretor", "categoria")
    search_fields = ("titulo",)
