import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class MaingSpider(scrapy.Spider):
    name = "bvsalud"
    allowed_domains = ['https://bvsalud.org/']
    start_urls = ['https://pesquisa.bvsalud.org/portal/?output=xml&lang=pt&from=0&sort=&format=summary&count=20&fb=&page=1&range_year_start=2015&range_year_end=2020&index=tw&q=Desastre+rompimento']

    BASE_URL = 'https://bvsalud.org/'


    def parse(self, response):
      for article in response.xpath("//response/result/doc").get():
       
        yield  self.parse_article(article)

          
    def parse_article(self, response):
        link   = response.url
        titulo  = response.css("h1.h1-regular-7::text").extract_first()
        dataPublicacao = self.data_parse(response.css("div.article__date").extract_first()) 
        conteudo  = ""
        for p in response.css("div.wpb_wrapper p"):
            conteudo  =  conteudo+"\n"+p.css("p ::text").extract_first()
        
        notice = SigdesastrescrapyItem(titulo=titulo, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)
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
            texto = "%s-%s-%s"%(data[3],meses[data[5]],data[7])
        except:
            print("erro ao converter data")

        return texto