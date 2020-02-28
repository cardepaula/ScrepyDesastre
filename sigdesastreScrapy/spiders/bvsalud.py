import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem


class MaingSpider(scrapy.Spider):
    name = "bvsalud"
    allowed_domains = ['https://bvsalud.org/']
    start_urls = [
        'https://pesquisa.bvsalud.org/portal/?output=xml&lang=pt&from=0&sort=&format=summary&count=20&fb=&page=1&range_year_start=2015&range_year_end=2020&index=tw&q=Desastre+rompimento',
        'https://pesquisa.bvsalud.org/portal/?output=xml&lang=pt&from=0&sort=&format=summary&count=20&fb=&page=1&range_year_start=2015&range_year_end=2020&index=tw&q=disaster+dam',
        'https://pesquisa.bvsalud.org/portal/?output=xml&lang=pt&from=0&sort=&format=summary&count=20&fb=&page=1&range_year_start=2015&range_year_end=2020&index=tw&q=disaster+samarco'
    ]

    BASE_URL = 'https://bvsalud.org/'

    # http://www.macoratti.net/vb_xpath.htm

    def parse(self, response):
        for article in response.xpath("//doc"):
            link = article.xpath(
                "//arr[@name='ur']").css("::text").extract_first()
            titulo = article.xpath(
                "//arr[@name='ti_pt']").css("::text").extract_first()
            dataPublicacao = self.data_parse(article.xpath(
                "//str[@name='da']").css("::text").extract_first())
            conteudo = article.xpath(
                "//arr[@name='ab_pt']").css("::text").extract_first()

            notice = SigdesastrescrapyItem(
                titulo=titulo, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)
            yield notice

    def doc_parse(self, response):
        pass

    def data_parse(self, data):
        texto = ""
        try:

            texto = "01-%s-%s" % (data[4:], data[:4])

        except:

            print("erro ao converter data")

        return texto
