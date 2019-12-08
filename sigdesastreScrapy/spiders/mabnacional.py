# coding=utf-8
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class MabnacionalSpider(scrapy.Spider):
    name = "mabnacional"
    allowed_domains = ['https://www.mabnacional.org.br']
    start_urls = ['https://www.mabnacional.org.br/search/node/Desastre%20Mariana?page=0',
                  'https://www.mabnacional.org.br/search/node/Desastre%20Mariana?page=1']

    def parse(self, response):
        for quote in response.css('div.search-result'):
            yield {
                'titulo': quote.css('a::text').extract_first(),
                'link': quote.css('a::attr(href)').extract_first(),
                'descricao': quote.css('p.search-snippet').extract_first(),
                'dataPublicacao': self.dateparse(quote.css('span.search-info-date::text').extract_first()) ,
                'dataCriacao': self.dateparse(quote.css('span.search-info-date::text').extract_first()),
                'dataAtualizacao': self.dateparse(quote.css('span.search-info-date::text').extract_first()),
                'conteudo': self.createconteudo(),
                'fonte':self.createfonte(),
                'midias': [],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }


    def dateparse(self, data):
        x = data.split()[1]
        x = x.split('/')
        return '%s-%s-%s' % (x[2],x[1],x[0])

    def createconteudo(self):
        return None

    def createfonte(self):
        return { 'nome': 'Movimento dos Atingidos por Barragens',
            'link': 'https://www.mabnacional.org.br',
            'descricao': '',
            'tipoFonte': {
            'id': 3,
            'nome': 'Associações e Movimentos'
            } }
    def createGrupoAcesso(self):
        return { 'id': 1, 'nome': 'todos',}