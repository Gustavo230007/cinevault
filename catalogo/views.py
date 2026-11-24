from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Categoria, Diretor, Filme

FILMES_POR_PAGINA = 5


def lista_filmes(request):
    # 1. Parâmetros recebidos via GET
    busca = request.GET.get("q", "").strip()
    diretor_id = request.GET.get("diretor", "")
    categoria_id = request.GET.get("categoria", "")

    # 2. Consulta base (select_related evita consultas extras por filme)
    filmes = Filme.objects.select_related("diretor", "categoria").order_by("titulo")

    # 3. Filtros aplicados ANTES da paginação (combináveis entre si)
    if busca:
        filmes = filmes.filter(titulo__icontains=busca)
    if diretor_id.isdigit():
        filmes = filmes.filter(diretor_id=diretor_id)
    if categoria_id.isdigit():
        filmes = filmes.filter(categoria_id=categoria_id)

    # 4. Paginação: 5 registros por página
    paginator = Paginator(filmes, FILMES_POR_PAGINA)
    page_obj = paginator.get_page(request.GET.get("page"))

    # 5. Querystring sem "page" para preservar filtros nos links de navegação
    params = request.GET.copy()
    params.pop("page", None)
    querystring = params.urlencode()

    contexto = {
        "page_obj": page_obj,
        "total_resultados": paginator.count,
        "diretores": Diretor.objects.all(),
        "categorias": Categoria.objects.all(),
        "busca": busca,
        "diretor_sel": diretor_id,
        "categoria_sel": categoria_id,
        "querystring": querystring,
    }
    return render(request, "catalogo/lista_filmes.html", contexto)
