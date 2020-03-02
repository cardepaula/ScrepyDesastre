# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from sigdesastreScrapy.items import SigdesastrescrapyItem


class MaingSpider(scrapy.Spider):
    name = "sitedelinhares"
    allowed_domains = ['sitedelinhares.com.br']
    start_urls = [
        'https://www.sitedelinhares.com.br/busca']

    BASE_URL = 'https://www.sitedelinhares.com.br/busca'

    def parse(self, response):
        formdata = {"keyword": "samarco"}
        yield FormRequest(self.BASE_URL, callback=self.post_request, formdata=formdata)

    def post_request(self, response):
        for article in response.css("a.noticia_box.geral"):
            link = article.css("a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("div.layout h1::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "li.data p::text").extract_first())

        conteudo = response.css("div.html_box p::text").extract_first('')
        conteudo = response.css("div.html_box div::text").extract_first('')

        notice = SigdesastrescrapyItem(
            titulo=titulo, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)
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
            texto = "%s-%s-%s" % (data[1], meses[data[3].lower()], data[5])
            # texto = data
        except:
            print(">>>>>> ERRO NA DATA")
        return texto
