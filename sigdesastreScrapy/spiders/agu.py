import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte


class MaingSpider(scrapy.Spider):
    name = "agu"
    allowed_domains = ['www.agu.gov.br']
    start_urls = ['https://www.agu.gov.br/busca/?texto=desastre+mariana&tipoConteudo%5B%5D=3&tipoConteudo%5B%5D=2&tipoConteudo%5B%5D=1&tipoPesquisa=1&Busca=Busca']

    BASE_URL = 'https://www.agu.gov.br'

    def parse(self, response):
        next_page = response.css('ul li.txt a::attr(href)').getall()[-2]
        if next_page is not None:
            print(">>>>>>>>>>>>>>>>>>>>>>proxima pagina>>>>>>>>>>>>>>>>>>>>>>")
            yield response.follow(self.BASE_URL+next_page, self.parse)

        for article in response.css("div.tileItem"):
            link = article.css("a.summary::attr(href)").extract_first()

            yield response.follow(self.BASE_URL+link, self.parse_article)

    def parse_article(self, response):

        link = response.url
        titulo = response.css("h3.outstanding-title::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "span.documentPublished span::text").getall()[1].split()[0])
        try:
            conteudo = ""
            for p in response.css("div.cell p"):
                conteudo = conteudo+"\n"+p.css("p ::text").extract_first()
        except:
            lista_conteudo = response.css("div.row div.cell::text").extract()
            for p in lista_conteudo:
                conteudo += p

        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []

        notice = SigdesastrescrapyItem(
            titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

        yield notice

    def data_parse(self, data):

        texto = ""
        try:
            data = data.split('/')
            texto = "%s-%s-%s" % (data[0], data[1], data[2])
        except:
            print("erro ao converter data")

        return texto
