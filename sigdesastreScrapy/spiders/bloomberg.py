import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class MaingSpider(scrapy.Spider):
    name = "bloomberg"
    allowed_domains = ['www.bloomberg.com.br']
    start_urls = ['https://www.bloomberg.com.br/?s=mariana+samarco&x=0&y=0']

    BASE_URL = 'https://www.bloomberg.com.br/'


    def parse(self, response):
      for article in response.css("div.search-result__content"):
        link    = article.css("a::attr(href)").extract_first()
        
        yield response.follow(link, self.parse_article)


    #   next_page = response.css('a#mais::attr(href)').extract_first()
    #   if next_page is not None:
    #       yield response.follow(next_page, self.parse)
          
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