# 🎬 CineVault — Catálogo de Filmes

**Disciplina:** Programação para Internet
**Tecnologia:** Python + Django 5
**Tema escolhido:** Catálogo de Filmes

## Integrantes da dupla
Gustavo Sousa Araújo
Jean Lucas Bezerra de Oliveira

## Descrição
Aplicação web que lista filmes e permite pesquisar, filtrar e paginar os registros.

### Modelos
- **Diretor** (`nome`, `nacionalidade`)
- **Categoria** (`nome`)
- **Filme** (`titulo`, `ano_lancamento`, `nota`, `sinopse`, `diretor` → FK, `categoria` → FK)

### Filtros implementados
| Filtro | Campo | Como funciona |
|---|---|---|
| Pesquisa textual | `q` | `Filme.objects.filter(titulo__icontains=q)` |
| Diretor | `<select name="diretor">` | `filter(diretor_id=...)` |
| Categoria | `<select name="categoria">` | `filter(categoria_id=...)` |

Todos usam o método **GET**, funcionam individualmente ou combinados e são aplicados **antes** da paginação.

### Paginação
`Paginator` com **5 filmes por página**, botões *Anterior/Próxima*, indicação "Página X de Y". Os filtros são preservados nos links porque a view monta uma querystring a partir de `request.GET` removendo apenas o parâmetro `page`.

## Como executar
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations catalogo
python manage.py migrate
python manage.py popular        # carrega 24 filmes, 6 diretores e 5 categorias
python manage.py createsuperuser  # opcional, para usar o /admin
python manage.py runserver
```
Acesse: http://127.0.0.1:8000/
