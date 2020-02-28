import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem


class MaingSpider(scrapy.Spider):
    name = "oolhar"
    allowed_domains = ['oolhar.com.br']
    start_urls = ['https://oolhar.com.br/?s=barragem+fundão']

    BASE_URL = 'https://oolhar.com.br'

    def parse(self, response):
        for article in response.css("main div.vw-post-box__content"):
            link = article.css(
                "a.vw-post-box__link::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

    #   next_page = response.css('a#mais::attr(href)').extract_first()
    #   if next_page is not None:
    #       yield response.follow(next_page, self.parse)
            pages = response.css('a.next.page-numbers::attr(href)')
            for a in pages:
                yield response.follow(a, self.parse)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1.vw-post-title::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "time::text").extract_first())
        conteudo = ""
        for p in response.css("div.vw-post-content.clearfix p"):
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
        texto = ""
        try:
            data = data.split('/')
            data[2] = data[2].split()[0]
            texto = "%s-%s-%s" % (data[0], data[1], data[2])
        except:
            print("erro ao converter data")

        return texto
