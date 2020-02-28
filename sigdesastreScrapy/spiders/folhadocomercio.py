import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

# TODO descobrir como capturar a data


class MaingSpider(scrapy.Spider):
    name = "folhadocomercio"
    allowed_domains = ['folhadocomercio.com.br']
    start_urls = [
        'http://www.folhadocomercio.com.br/folha-do-comercio/?s=barragem']

    BASE_URL = 'http://www.folhadocomercio.com.br'

    def parse(self, response):
        for article in response.css("article"):
            link = article.css(
                "div.dash a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

        next_page = response.css('p.pageNext a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            # pages = response.css('p.pageNext a::attr(href)')
            # for a in pages:
            #     yield response.follow(a, self.parse)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1::text").extract_first()
        titulo += response.css("h1 span::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "time::text").extract_first())
        conteudo = ""
        for p in response.css("div.bt_bb_wrapper"):
            conteudo = conteudo+"\n"+p.css("p ::text").extract_first()

        notice = SigdesastrescrapyItem(
            titulo=titulo, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)
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
        texto = "01-01-2020"

        return texto
