# coding=utf-8
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
import datetime


class EcoaSpider(scrapy.Spider):
    name = "samarco"
    allowed_domains = ['samarco.com']
    start_urls = ['https://www.samarco.com/?s=desastre+mariana']

    def parse(self, response):
        for quote in response.css('div.noticia-box'):
            yield {
                'link': (quote.css('a.noticia-titulo::attr(href)').extract_first()) ,
                'descricao': quote.css('a.noticia-titulo::text').extract_first(),
                'dataPublicacao': self.dateparse(quote.css('p.noticia-data::text').extract_first()) ,
                'titulo': quote.css('a.noticia-titulo::text').extract_first(),
                'conteudo': self.createconteudo(),
                'dataCriacao': self.dateparse(quote.css('p.noticia-data::text').extract_first()),
                'dataAtualizacao': self.dateparse(quote.css('p.noticia-data::text').extract_first()),
                'fonte':self.createfonte(),
                'midias': [],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }


    def dateparse(self,data):
        d = data.split('/')
        return "%s-%s-%s"%(d[0],d[1],d[2])

    def parselink(self,link):
        if link[0] != 'h':
            return 'https://www.samarco.com/' + link
        else: return link

    def createconteudo(self):
        return None
    def createfonte(self):
        return { 'nome': 'samarco',
            'link': 'https://www.samarco.com/',
            'descricao': 'Samarco é uma empresa de capital fechado que atua no segmento de mineração.',
            'tipoFonte': {
            'id': 6,
            'nome': 'Iniciativa Privada'
            } }
    def createGrupoAcesso(self):
        return { 'id': 1, 'nome': 'todos',}