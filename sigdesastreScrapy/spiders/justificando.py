import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte

# TODO identificar problema de repetição


class MaingSpider(scrapy.Spider):
    name = "justificando"
    allowed_domains = ['justificando.com']
    start_urls = [
        'http://www.justificando.com/?s=desastre+samarco&search_button=Buscar+']

    BASE_URL = 'http://www.justificando.com'

    def parse(self, response):
        next_page = response.css(
            'a.next.page-numbers::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

            
        for article in response.css("article"):
            link = article.css("a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)




    def parse_article(self, response):

        try:
            link = response.url
            titulo = response.css("h4 a::text").extract_first()
            dataPublicacao = self.data_parse(response.css(
                "span.entry-tdate::text").extract_first())
            conteudo = ""
            for p in response.css("div.entry-content p"):
                conteudo = conteudo+"\n"+p.css("p ::text").extract_first()
        except:
            conteudo = "404"

        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []

        notice = SigdesastrescrapyItem(
            titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

        yield notice

    def data_parse(self, data):

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
        texto = ""
        try:
            data = data.split()
            texto = "%s-%s-%s" % (data[1], meses[data[3]], data[5])
        except:
            print("erro ao converter data")

        return texto
