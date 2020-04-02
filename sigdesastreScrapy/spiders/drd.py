import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte


class MaingSpider(scrapy.Spider):
    name = "drd"
    allowed_domains = ['drd.com.br']
    start_urls = ['https://drd.com.br/?s=desastre+mariana']

    BASE_URL = 'https://drd.com.br/'

    def parse(self, response):
        for article in response.css("article"):
            link = article.css("a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

    #   next_page = response.css('a#mais::attr(href)').extract_first()
    #   if next_page is not None:
    #       yield response.follow(next_page, self.parse)
            pages = response.css('a.page_nav.next::attr(href)')
            for a in pages:
                yield response.follow(a, self.parse)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "div.jeg_meta_date a::text").extract_first())
        conteudo = ""
        for p in response.css("div.content-inner p"):
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

        meses = {"janeiro": 1,
                 "fevereiro": 2,
                 "março": 3,
                 "abril": 4,
                 "maio": 5,
                 "junho": 6,
                 "julho": 7,
                 "agosto": 8,
                 "setembro": 9,
                 "outubro": 10,
                 "novembro": 11,
                 "dezembro": 12
                 }
        texto = ""
        try:
            data = data.split()
            data[1] = data[1][:-1]
            texto = "%s-%s-%s" % (data[1], meses[data[0]], data[2])
        except:
            print("erro ao converter data")

        return texto

    def createfonte(self):
        return {'nome': 'Site de Linhares',
                'link': 'https://www.sitedelinhares.com.br/',
                'descricao': 'Site de Linhares',
                'tipoFonte': {
                    'id': 1,
                    'nome': 'Fontes Oficiais'
                }}
