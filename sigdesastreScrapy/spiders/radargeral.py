# -*- coding: utf-8 -*-
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem


class MaingSpider(scrapy.Spider):
    name = "radargeral"
    allowed_domains = ['radargeral.com']
    start_urls = [
        'https://radargeral.com/page/1/?s=barragem+fund%C3%A3o']

    BASE_URL = 'https://radargeral.com'

    def parse(self, response):
        for article in response.css("main.site-main article"):
            link = article.css("h2 a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

        next_page = response.css(
            'div.nav-previous a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            # pages = response.css('p.pageNext a::attr(href)')
            # for a in pages:
            #     yield response.follow(a, self.parse)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1.entry-title::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "time.entry-date::attr(datetime)").extract_first())

        conteudo = ""
        result = response.css("div.entry-content h1::text").extract_first()
        if result is not None:
            conteudo += result

        for p in response.css("div.entry-content h3"):
            result = p.css("h3 ::text").extract_first()
            if result is not None:
                conteudo += "\n" + result

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
            data = data.split('T')[0]
            data = data.split('-')
            texto = "%s-%s-%s" % (data[2], data[1], data[0])
        except:
            print(">>>>>> ERRO NA DATA")
        return texto
