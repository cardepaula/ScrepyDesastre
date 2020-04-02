import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte

# TODO fazer paginação


class MaingSpider(scrapy.Spider):
    name = "portalminas"
    allowed_domains = ['portalminas.com']
    start_urls = [
        'https://www.portalminas.com/ajax.php?case=ajax_search_next_prev&page=1&q=barragem']

    BASE_URL = 'https://www.portalminas.com/ajax.php?case=ajax_search_next_prev&page='
    QUERY = "&q=barragem"
    COUNT = 1

    def parse(self, response):
        try:
            for article in response.css("div.section-news"):
                link = article.css("a::attr(href)").extract_first()

                yield response.follow(link, self.parse_article)
        except:

            self.COUNT = 0
    #   next_page = response.css('a#mais::attr(href)').extract_first()
    #   if next_page is not None:
    #       yield response.follow(next_page, self.parse)

            # pages = response.css('a.page_nav.next::attr(href)')
            # for a in pages:
            #     yield response.follow(a, self.parse)
            while COUNT > 0:
                yield response.follow(self.BASE_URL+self.COUNT+self.QUERY, self.parse)
                self.COUNT += 1

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1.heading-font a::text").extract_first()
        dataPublicacao = self.data_parse(response.xpath(
            "//meta[@property='article:published_time']").css('::attr(content)').extract_first())
        conteudo = ""
        for p in response.css("div.article-content p"):
            conteudo = conteudo+"\n"+p.css("p ::text").extract_first()

        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []

        notice = SigdesastrescrapyItem(
            titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

        yield notice

    def data_parse(self, data):

        # meses = {"janeiro": 1,
        #          "fevereiro": 2,
        #          "março": 3,
        #          "abril": 4,
        #          "maio": 5,
        #          "junho": 6,
        #          "julho": 7,
        #          "agosto": 8,
        #          "setembro": 9,
        #          "outubro": 10,
        #          "novembro": 11,
        #          "dezembro": 12
        #          }
        texto = ""
        try:
            data = data.split('T')
            data = data[0].split('-')
            texto = "%s-%s-%s" % (data[2], data[1], data[0])
        except:
            print(">>>>>>>>>>>>>>>>>>>>>> erro ao converter data %s" % data)

        return texto
