import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte

# TODO site protegido


class MaingSpider(scrapy.Spider):
    name = "bloomberg"
    allowed_domains = ['www.bloomberg.com.br']
    start_urls = ['https://www.bloomberg.com.br/?s=mariana+samarco&x=0&y=0']
    BASE_URL = 'https://www.bloomberg.com.br/'

    # def start_requests(self):
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Cache-Control': 'max-age=0',
    #         'DNT': '1',
    #         'Upgrade-Insecure-Requests': '1',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    #         'Sec-Fetch-User': '?1',
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'navigate',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #     return [scrapy.FormRequest('https://www.bloomberg.com.br/?s=mariana+samarco&x=0&y=0',
    #                                headers=headers)]

    def parse(self, response):
        for article in response.css("div.search-result__content"):
            link = article.css("a::attr(href)").extract_first()
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        link = response.url
        titulo = response.css("h1.h1-regular-7::text").extract_first()
        dataPublicacao = self.data_parse(
            response.css("div.article__date").extract_first())
        conteudo = ""
        for p in response.css("div.wpb_wrapper p"):
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
        data = data.split()
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
            texto = "%s-%s-%s" % (data[3], meses[data[5]], data[7])
        except:
            print("erro ao converter data")

        return texto
