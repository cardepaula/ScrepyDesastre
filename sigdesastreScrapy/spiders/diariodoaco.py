import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte


class MaingSpider(scrapy.Spider):
    name = "diariodoaco"
    allowed_domains = ['diariodoaco.com.br']
    start_urls = [
        'https://www.diariodoaco.com.br/pesquisa/?t=barragem+fund%C3%A3o']

    BASE_URL = 'https://www.diariodoaco.com.br'

    def parse(self, response):
        for article in response.css("div.col-md-8 article"):
            link = article.css("a::attr(href)").extract_first()[1:]

            yield response.follow(self.BASE_URL + link, self.parse_article)

    #   next_page = response.css('a#mais::attr(href)').extract_first()
    #   if next_page is not None:
    #       yield response.follow(next_page, self.parse)
            # pages = response.css('a.page_nav.next::attr(href)')
            # for a in pages:
            #     yield response.follow(a, self.parse)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1.article-title b::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "ul.article-meta li::text").extract_first())
        conteudo = ""
        for p in response.css("div.textoNoticia::text").getall():
            conteudo = conteudo+"\n"+p

        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []

        notice = SigdesastrescrapyItem(
            titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

        yield notice

    def data_parse(self, data):

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
            data = data.split()[0]
            data = data.split('/')
            texto = "%s-%s-%s" % (data[0], data[1], data[2])
        except:
            print("erro ao converter data")

        return texto
