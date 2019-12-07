# coding=utf-8
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class GlobalSpider(scrapy.Spider):
    name = "global"
    allowed_domains = ['http://www.global.org.br']
    start_urls = ['http://www.global.org.br/page/1/?s=desastre+de+mariana',
                  'http://www.global.org.br/page/2/?s=desastre+de+mariana',
                  'http://www.global.org.br/page/3/?s=desastre+de+mariana']

    def parse(self, response):
        for quote in response.css('ul.search-list li'):
            yield {
                'titulo': quote.css('h2 a::text').extract_first(),
                'link': quote.css('h2 a::attr(href)').extract_first(),
                'descricao': quote.css('p a::text').extract_first(),
                'dataPublicacao': self.dateparse(quote.css('time p::text').extract_first()) ,
                'dataCriacao': self.dateparse(quote.css('time p::text').extract_first()),
                'dataAtualizacao': self.dateparse(quote.css('time p::text').extract_first()),
                'conteudo': self.createconteudo(),
                'fonte':self.createfonte(),
                'midias': [],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }
        for quote in response.css('ul.search-list li'):
            pass

    def dateparse(self, data):
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
        x = data.split()
        return '%s-%s-%s' % (x[4], meses[x[2]], x[0])

    def createconteudo(self):
        return None

    def createfonte(self):
        return { 'nome': 'Justiça Global',
            'link': 'http://www.global.org.br/',
            'descricao': '',
            'tipoFonte': {
            'id': 3,
            'nome': 'Associações e Movimentos'
            } }
    def createGrupoAcesso(self):
        return { 'id': 1, 'nome': 'todos',}