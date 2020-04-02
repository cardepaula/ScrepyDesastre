# -*- coding: utf-8 -*-
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte


class MaingSpider(scrapy.Spider):
    name = "correiodoestadoonline"
    allowed_domains = ['correiodoestadoonline.com.br']
    start_urls = [
        'http://www.correiodoestadoonline.com.br/busca/samarco/1']

    BASE_URL = 'http://www.correiodoestadoonline.com.br'

    def parse(self, response):
        for article in response.css("li.li-anuncio"):
            link = article.css("a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

        # next_page = response.css(
        #     'div.nav-previous a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)

            # pages = response.css('p.pageNext a::attr(href)')
            # for a in pages:
            #     yield response.follow(a, self.parse)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("div.noticia h1::text").extract_first()
        dataPublicacao = self.data_parse(response.css(
            "div.noticia h2::text").extract_first())

        conteudo = ""
        for p in response.css("div.texto "):
            result = p.css("p span::text").extract_first()
            if result is not None:
                conteudo += "\n" + result

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
            texto = "%s-%s-%s" % (data[0], meses[data[2].lower()], data[4])
        except:
            print(">>>>>> ERRO NA DATA")
        return texto
