import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte


class MaingSpider(scrapy.Spider):
    name = "sonhoseguro"
    allowed_domains = ['www.sonhoseguro.com.br']
    start_urls = ['https://www.sonhoseguro.com.br/?s=mariana+samarco']

    BASE_URL = 'https://www.sonhoseguro.com.br/'

    def parse(self, response):
        for article in response.css("h2.entry-title"):
            link = article.css("a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

        next_page = response.css(
            'a.next.page-numbers::attr(href)').extract_first()
        if next_page is not None:
            print(">>>>>foi para proxima pagina>>>>>>")
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1.entry-title::text").extract_first()
        dataPublicacao = self.data_parse(
            response.css("span.updated::text").extract_first())
        conteudo = ""
        for p in response.css("div.entry-content p"):
            conteudo = conteudo+"\n"+p.css("p ::text").extract_first()
        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []

        notice = SigdesastrescrapyItem(
            titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

        yield notice

    def data_parse(self, data):
        data = data.split()
        data = data[0].split('/')
        # meses = {"janeiro": 1,
        #          "fevereiro": 2,
        #          "março": 3,
        #          "abril": 4,
        #          "maio": 5,
        #          "junho": 6,
        #          "julho": 7,
        #          "agosto": 8,
        #          "setembro": 9,
        #          "outubro": 10,
        #          "novembro": 11,
        #          "dezembro": 12
        #          }
        texto = ""
        try:
            texto = "%s-%s-%s" % (data[0], data[1], data[2])
        except:
            print("erro ao converter data")

        return texto

    def createfonte(self):
        return {'nome': 'Sonho Seguro',
                'link': 'www.sonhoseguro.com.br',
                'descricao': 'Site de seguros',
                'tipoFonte': {
                    'id': 6,
                    'nome': 'Iniciativa Privada'
                }}
