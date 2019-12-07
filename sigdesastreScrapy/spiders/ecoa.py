# coding=utf-8
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
import datetime


class EcoaSpider(scrapy.Spider):
    name = "ecoa"
    allowed_domains = ['ecoa.org.br']
    start_urls = ['https://ecoa.org.br/?s=desastre+mariana']

    def parse(self, response):
        for quote in response.css('a.m-miniatura.foto-internas.grid'):
            yield {
                'link': self.parselink(quote.css('a.m-miniatura.foto-internas.grid ::attr(href)').extract_first()) ,
                'descricao': quote.css('span.m-miniatura__resumo p ::text').extract_first(),
                'dataPublicacao': self.dateparse() ,
                'titulo': quote.css('h1.m-miniatura__titulo::text').extract_first(),
                'conteudo': self.createconteudo(),
                'dataCriacao': self.dateparse(),
                'dataAtualizacao': self.dateparse(),
                'fonte':self.createfonte(),
                'midias': [],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }


    def dateparse(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def parselink(self,link):
        if link[0] != 'h':
            return 'https://ecoa.org.br/' + link
        else: return link

    def createconteudo(self):
        return None
    def createfonte(self):
        return { 'nome': 'ecoa',
            'link': 'https://ecoa.org.br',
            'descricao': 'Ecoa – Ecologia e Ação de Campo Grande, capital de Mato Grosso do Sul.',
            'tipoFonte': {
            'id': 3,
            'nome': 'Associações e Movimentos'
            } }
    def createGrupoAcesso(self):
        return { 'id': 1, 'nome': 'todos',}