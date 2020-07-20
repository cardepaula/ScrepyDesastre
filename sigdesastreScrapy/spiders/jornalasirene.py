import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte
from datetime import datetime


class MaingSpider(scrapy.Spider):
    name = "jornalasirene"
    allowed_domains = ['jornalasirene.com.br', 'http://jornalasirene.com.br/']
    start_urls = ['http://jornalasirene.com.br/page/1?s=barragem+fund%C3%A3o',
                  'http://jornalasirene.com.br/?s=desastre+mariana']
    BASE_URL = 'https://www.agu.gov.br'

    def parse(self, response):
        for article in response.css("article.post h3"):
            link = article.css("a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

        next_page = response.css('a.next::attr(href)').extract_first()
        yield response.follow(next_page, self.parse)

    def parse_article(self, response):

        link = response.url
        titulo = response.css(
            "h1::text").extract_first('') + response.css(
            "h1 a::text").extract_first('')
        dataPublicacao = self.data_parse(
            response.css('time.time::attr(datetime)').extract_first())

        conteudo = ""

        for p in response.css("article"):
            conteudo = conteudo+"\n" + \
                p.xpath("//p/span/text()").extract_first('') + \
                p.xpath("//p/text()").extract_first('') +\
                p.xpath('//div/p/text()').extract_first('')

        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []

        notice = SigdesastrescrapyItem(
            titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

        yield notice

    def data_parse(self, data):
        texto = ''

        try:
            data = datetime.fromisoformat(str(data))
            texto = data.strftime("%d/%m/%Y")

        except:
            print("erro ao converter data")

        return texto
