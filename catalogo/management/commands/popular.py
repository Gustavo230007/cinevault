from decimal import Decimal

from django.core.management.base import BaseCommand

from catalogo.models import Categoria, Diretor, Filme

DIRETORES = [
    ("Christopher Nolan", "Reino Unido"),
    ("Quentin Tarantino", "Estados Unidos"),
    ("Denis Villeneuve", "Canadá"),
    ("Fernando Meirelles", "Brasil"),
    ("Jordan Peele", "Estados Unidos"),
    ("Edgar Wright", "Reino Unido"),
]

CATEGORIAS = ["Ação", "Drama", "Ficção Científica", "Terror", "Comédia"]

# (título, ano, nota, diretor, categoria, sinopse)
FILMES = [
    ("A Origem", 2010, "8.8", "Christopher Nolan", "Ficção Científica", "Ladrões invadem sonhos para plantar uma ideia."),
    ("Interestelar", 2014, "8.7", "Christopher Nolan", "Ficção Científica", "Astronautas buscam um novo lar para a humanidade."),
    ("Batman: O Cavaleiro das Trevas", 2008, "9.0", "Christopher Nolan", "Ação", "Batman enfrenta o Coringa em Gotham."),
    ("Dunkirk", 2017, "7.8", "Christopher Nolan", "Ação", "A evacuação de soldados aliados na Segunda Guerra."),
    ("Pulp Fiction", 1994, "8.9", "Quentin Tarantino", "Drama", "Histórias cruzadas de criminosos em Los Angeles."),
    ("Kill Bill: Vol. 1", 2003, "8.1", "Quentin Tarantino", "Ação", "Uma noiva busca vingança contra seus antigos aliados."),
    ("Bastardos Inglórios", 2009, "8.4", "Quentin Tarantino", "Drama", "Soldados planejam derrubar o regime nazista."),
    ("Django Livre", 2012, "8.5", "Quentin Tarantino", "Ação", "Um ex-escravo e um caçador de recompensas."),
    ("Duna", 2021, "8.0", "Denis Villeneuve", "Ficção Científica", "Paul Atreides chega ao planeta Arrakis."),
    ("Duna: Parte Dois", 2024, "8.5", "Denis Villeneuve", "Ficção Científica", "A jornada de Paul entre os Fremen."),
    ("Blade Runner 2049", 2017, "8.0", "Denis Villeneuve", "Ficção Científica", "Um novo blade runner descobre um segredo antigo."),
    ("Sicario: Terra de Ninguém", 2015, "7.6", "Denis Villeneuve", "Ação", "Uma agente do FBI na guerra contra o cartel."),
    ("Cidade de Deus", 2002, "8.6", "Fernando Meirelles", "Drama", "O crescimento do crime em uma favela do Rio."),
    ("Ensaio sobre a Cegueira", 2008, "6.6", "Fernando Meirelles", "Drama", "Uma epidemia de cegueira atinge uma cidade."),
    ("Os Dois Papas", 2019, "7.5", "Fernando Meirelles", "Drama", "O encontro entre Bento XVI e Francisco."),
    ("O Jardineiro Fiel", 2005, "7.4", "Fernando Meirelles", "Drama", "Um diplomata investiga a morte da esposa."),
    ("Corra!", 2017, "7.6", "Jordan Peele", "Terror", "Um jovem visita a família da namorada."),
    ("Nós", 2019, "6.8", "Jordan Peele", "Terror", "Uma família é atacada por seus duplos."),
    ("Não! Não Olhe!", 2022, "6.8", "Jordan Peele", "Terror", "Irmãos descobrem algo estranho nos céus."),
    ("Todo Mundo Quase Morto", 2004, "7.9", "Edgar Wright", "Comédia", "Dois amigos enfrentam uma invasão zumbi."),
    ("Chumbo Grosso", 2007, "7.8", "Edgar Wright", "Comédia", "Um policial exemplar é enviado a uma vila tranquila."),
    ("Em Ritmo de Fuga", 2017, "7.6", "Edgar Wright", "Ação", "Um motorista de fuga vive ao som da trilha."),
    ("Scott Pilgrim Contra o Mundo", 2010, "7.5", "Edgar Wright", "Comédia", "Scott luta contra os ex-namorados de Ramona."),
    ("Oppenheimer", 2023, "8.3", "Christopher Nolan", "Drama", "A criação da bomba atômica."),
]


class Command(BaseCommand):
    help = "Popula o banco com diretores, categorias e filmes de exemplo."

    def handle(self, *args, **options):
        diretores = {}
        for nome, nac in DIRETORES:
            diretores[nome], _ = Diretor.objects.get_or_create(nome=nome, defaults={"nacionalidade": nac})

        categorias = {}
        for nome in CATEGORIAS:
            categorias[nome], _ = Categoria.objects.get_or_create(nome=nome)

        criados = 0
        for titulo, ano, nota, dir_nome, cat_nome, sinopse in FILMES:
            _, created = Filme.objects.get_or_create(
                titulo=titulo,
                defaults={
                    "ano_lancamento": ano,
                    "nota": Decimal(nota),
                    "sinopse": sinopse,
                    "diretor": diretores[dir_nome],
                    "categoria": categorias[cat_nome],
                },
            )
            criados += created

        self.stdout.write(self.style.SUCCESS(f"{criados} filmes criados (total: {Filme.objects.count()})."))
