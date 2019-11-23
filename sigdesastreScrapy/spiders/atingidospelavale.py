import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem


class AtingidospelavaleSpider(scrapy.Spider):
    name = "atingidospelavale"
    allowed_domains = ['atingidospelavale.wordpress.com']
    start_urls = ['https://atingidospelavale.wordpress.com/?s=desastre+mariana']

    def parse(self, response):
        for quote in response.css('div.post-container'):
            yield {
                'link': quote.css('h1.post-title a::attr(href)').extract_first() ,
                'descricao': quote.css('div.post-content p::text').extract_first(),
                'dataPublicacao': quote.css('time.updated::attr(datetime)').extract_first() ,
                'titulo': quote.css('h1.post-title a::text').extract_first(),
                'conteudo': self.createconteudo(),
                'dataCriacao': quote.css('time.updated::attr(datetime)').extract_first(),
                'dataAtualizacao': quote.css('time.updated::attr(datetime)').extract_first(),
                'fonte':self.createfonte(),
                'midias': [quote.css('img::attr(src)').extract_first()],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }


    def createconteudo(self):
        return None
    def createfonte(self):
        return { 'nome': 'atingidospelavale',
            'link': 'https://atingidospelavale.wordpress.com',
            'descricao': 'Nacional',
            'tipoFonte': {
            'id': 4,
            'nome': 'Midias Sociais'
            } }
    def createGrupoAcesso(self):
        return { 'id': 1, 'nome': 'todos'}