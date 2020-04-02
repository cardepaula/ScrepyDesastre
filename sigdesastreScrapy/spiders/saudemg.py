# coding=utf-8

import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte


class SaudemgSpider(scrapy.Spider):
    name = "saudemg"
    allowed_domains = ['saude.mg.gov.br']
    start_urls = ['http://saude.mg.gov.br/component/search/?all=desastre+mariana&exact=&any=&none=&created=&modified=&area=all',
                  'http://saude.mg.gov.br/component/search/?all=rompimento%20barragem&exact=&any=&none=&created=&modified=&from=40&area=stories',
                  'http://saude.mg.gov.br/component/search/?all=rompimento%20barragem&exact=&any=&none=&created=&modified=&from=0&area=stories']

    def parse(self, response):
        for quote in response.css('div.card'):

            yield {
                'link': self.parselink(quote.css('h2.title a ::attr(href)').extract_first()),
                'descricao': quote.css('div.description p ::text').extract_first(),
                'dataPublicacao': self.dateparse(quote.css('span.date ::text').extract_first()),
                'titulo': quote.css('h2.title a ::text').extract_first(),
                'conteudo': self.createconteudo(),
                'dataCriacao': self.dateparse(quote.css('span.date ::text').extract_first()),
                'dataAtualizacao': self.dateparse(quote.css('span.date ::text').extract_first()),

                'fonte': self.createfonte(),
                'midias': [],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }

    def dateparse(self, data):
        meses = {"Janeiro": 1,
                 "Fevereiro": 2,
                 "Março": 3,
                 "Abril": 4,
                 "Maio": 5,
                 "Junho": 6,
                 "Julho": 7,
                 "Agosto": 8,
                 "Setembro": 9,
                 "Outubro": 10,
                 "Novembro": 11,
                 "Dezembro": 12
                 }
        x = data.split()
        return '%s-%s-%s' % (x[4], meses[x[2]], x[0])

    def parselink(self, link):
        if link[0] != 'h':
            return 'http://saude.mg.gov.br' + link
        else:
            return link

    def createconteudo(self):
        return None

    def createfonte(self):
        cf = Fonte()
        fonte = cf.createFonte(self.name)

    def createGrupoAcesso(self):
        cf = Fonte()
        grupoAcesso = cf.GRUPOACESSO
