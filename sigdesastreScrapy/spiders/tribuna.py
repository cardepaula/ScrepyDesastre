import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte
from datetime import datetime
import re


class MaingSpider(scrapy.Spider):
    name = "tribuna"
    allowed_domains = ['tribunaonline.com.br']
    start_urls = ['https://tribunaonline.com.br/search?q=barragem']
    BASE_URL = 'https://tribunaonline.com.br'

    def parse(self, response):
        for article in response.css("div.col-sm-8"):
            link = article.css("h3 a::attr(href)").extract_first()

            yield response.follow(self.BASE_URL+link, self.parse_article)

    def parse_article(self, response):

        link = response.url
        titulo = response.css(
            "h1.featured-title::text").extract_first('') + response.css("h5::text").extract_first('')
        dataPublicacao = self.data_parse(response.css(
            "span.text-muted::text").extract_first()) or self.data_parse(response.css("h6 i::text").extract_first())

        sep = ','
        conteudo = sep.join(response.css('div.content-block p::text').getall())

        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []

        notice = SigdesastrescrapyItem(
            titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

        yield notice

    def data_parse(self, data):
        data = re.search(r'(\d+/\d+/\d+)', data)
        return data.group()
