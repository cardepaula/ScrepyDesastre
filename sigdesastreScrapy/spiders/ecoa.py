import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem


class EcoaSpider(scrapy.Spider):
    name = "ecoa"
    allowed_domains = ['ecoa.org.br']
    start_urls = ['https://ecoa.org.br/?s=desastre+mariana']

    def parse(self, response):
        for quote in response.css('a.m-miniatura.foto-internas.grid'):
            yield {
                'link': self.parselink(quote.css('a.m-miniatura.foto-internas.grid ::attr(href)').extract_first()) ,
                'descricao': quote.css('span.m-miniatura__resumo p ::text').extract_first(),
                'dataPublicacao': self.dateparse(quote.css('span.date ::text').extract_first()) ,
                'titulo': quote.css('h1.m-miniatura__titulo::text').extract_first(),
                'conteudo': self.createconteudo(),
                'dataCriacao': self.dateparse(quote.css('span.date ::text').extract_first()),
                'dataAtualizacao': self.dateparse(quote.css('span.date ::text').extract_first()),
                'fonte':self.createfonte(),
                'midias': [],
                'grupoAcesso': self.createGrupoAcesso(),
                'descritores': []
            }


    def dateparse(self,data):
        meses = {"Janeiro":1,
                 "Fevereiro":2,
                 "Março":3,
                 "Abril":4,
                 "Maio":5,
                 "Junho":6,
                 "Julho":7,
                 "Agosto":8,
                 "Setembro":9,
                 "Outubro":10,
                 "Novembro":11,
                 "Dezembro":12
                 }
        x = data.split()
        return '%s-%s-%s' %(x[4],meses[x[2]],x[0])

    def parselink(self,link):
        if link[0] != 'h':
            return 'http://saude.mg.gov.br' + link
        else: return link

    def createconteudo(self):
        return None
    def createfonte(self):
        return { 'nome': 'Saude MG',
            'link': 'https://www.saude.mg.gov.br',
            'descricao': 'Belo Horizonte',
            'tipoFonte': {
            'id': 1,
            'nome': 'Fontes Oficiais'
            } }
    def createGrupoAcesso(self):
        return { 'id': 1, 'nome': 'todos',}