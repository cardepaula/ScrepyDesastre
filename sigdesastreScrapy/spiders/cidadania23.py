# coding=utf-8
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class cidadania23Spider(scrapy.Spider):
    name = "cidadania23"
    allowed_domains = ['https://cidadania23.org.br']
    start_urls = ['https://cidadania23.org.br/?s=desastre+mariana']

    def parse(self, response):
        for quote in response.css('article'):
            yield {
                'titulo': quote.css('h2 a::text').extract_first(),
                'link': quote.css('h2 a::attr(href)').extract_first(),
                'descricao': quote.css('div.jupiterx-post-content p::text').extract_first(),
                'dataPublicacao': self.dateparse(quote.css('h2 a::attr(href)').extract_first()) ,
                'dataCriacao': self.dateparse(quote.css('h2 a::attr(href)').extract_first()),
                'dataAtualizacao': self.dateparse(quote.css('h2 a::attr(href)').extract_first()),
                'conteudo': self.createconteudo(),
                'fonte':self.createfonte(),
                'midias': [],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }


    def dateparse(self, data):
        try:
            x = data.split('/')
            return '%s-%s-%s' % (x[3], x[4], x[5])
        except: ''

    def createconteudo(self):
        return None

    def createfonte(self):
        return { 'nome': 'Movimento dos Atingidos por Barragens',
            'link': 'https://cidadania23.org.br',
            'descricao': '',
            'tipoFonte': {
            'id': 3,
            'nome': 'Associações e Movimentos'
            } }
    def createGrupoAcesso(self):
        return { 'id': 1, 'nome': 'todos',}