# coding=utf-8
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem


class organonSpider(scrapy.Spider):
    name = "organon"
    allowed_domains = ['organon.ufes.br']
    start_urls = ['http://organon.ufes.br/noticias/?pag=1',
                  'http://organon.ufes.br/noticias/?pag=2',
                  'http://organon.ufes.br/noticias/?pag=3',
                  'http://organon.ufes.br/noticias/?pag=4',
                  'http://organon.ufes.br/noticias/?pag=5',
                  'http://organon.ufes.br/noticias/?pag=6',
                  'http://organon.ufes.br/noticias/?pag=7',
                  'http://organon.ufes.br/noticias/?pag=8']

    def parse(self, response):
        for quote in response.css('div a.opiniao'):
            yield {
                'link': self.parselink(quote.css('a.opiniao::attr(href)').extract_first()) ,
                'descricao': quote.css('p.description::text').extract_first(),
                'dataPublicacao': self.dateparse(quote.css('div.content strong::text').extract_first()) ,
                'titulo': quote.css('p.description::text').extract_first(),
                'conteudo': self.createconteudo(),
                'dataCriacao': self.dateparse(quote.css('div.content strong::text').extract_first()),
                'dataAtualizacao': self.dateparse(quote.css('div.content strong::text').extract_first()),
                'fonte':self.createfonte(),
                'midias': [],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }


    def dateparse(self,data):
        x = data.split('/')
        return '%s-%s-%s' %(x[2],x[1],x[0])

    def parselink(self, link):
        if link[0] != 'h':
            return 'http://organon.ufes.br/' + link
        else: return link

    def createconteudo(self):
        return None
    def createfonte(self):
        return { 'nome': 'Organon UFES',
            'link': 'http://organon.ufes.br',
            'descricao': "Núcleo de Estudo, Pesquisa e Extensão em Mobilizações Sociais",
            'tipoFonte': {
            'id': 2,
            'nome': 'Ciência'
            } }
    def createGrupoAcesso(self):
        return { 'id': 1, 'nome': 'todos',}