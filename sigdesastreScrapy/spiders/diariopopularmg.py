import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

# TODO descobrir como capturar a data


class MaingSpider(scrapy.Spider):
    name = "diariopopularmg"
    allowed_domains = ['diariopopularmg.com.br']
    start_urls = [
        'http://www.diariopopularmg.com.br/?s=desastre+mariana']

    BASE_URL = 'http://www.diariopopularmg.com.br'

    def parse(self, response):
        for article in response.css("div.main-content article"):
            link = article.css(
                "a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

        next_page = response.css(
            'a.next.page-numbers::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            # pages = response.css('p.pageNext a::attr(href)')
            # for a in pages:
            #     yield response.follow(a, self.parse)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1.entry-title::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "time::text").extract_first())
        conteudo = ""
        for p in response.css("div.entry-content p"):
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
        try:
            data = data.split('/')
            texto = "%s-%s-%s" % (data[0], data[1], data[2])
        except:
            print(">>>>>> ERRO NA DATA")
        return texto
