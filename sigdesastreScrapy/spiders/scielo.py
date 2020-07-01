import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte

# todo não terminado


class MaingSpider(scrapy.Spider):
    name = "scielo"
    allowed_domains = ['search.scielo.org', 'scielo.br', 'scielo.org.co']
    start_urls = [
        'https://search.scielo.org/?lang=pt&count=15&from=0&output=site&sort=&format=summary&fb=&page=1&q=Desastre+rompimento#',
        'https://search.scielo.org/?q=Desastre+rompimento&lang=pt&count=15&from=0&output=site&sort=&format=summary&fb=&page=1&q=desastre+samarco&lang=pt&page=1',
        'https://search.scielo.org/?q=desastre+samarco&lang=pt&count=15&from=0&output=site&sort=&format=summary&fb=&page=1&q=disaster+samarco&lang=pt&page=1']

    def parse(self, response):

        link = response.css("div.item a::attr(href)").extract()

        titulo = response.css("div.item strong.title::text").extract()
        dataPublicacao = response.css("div.item strong.title::text").extract()

        conteudo = response.css(
            "div.item div.abstract::text").extract()
        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []
        for i in range(len(link)):

            notice = SigdesastrescrapyItem(
                titulo=titulo[i], conteudo=conteudo[i], link=link[i], dataPublicacao=dataPublicacao, fonte=fonte, grupoAcesso=grupoAcesso, descritores=descritores, midias=midias)
            yield notice
