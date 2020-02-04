import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class MaingSpider(scrapy.Spider):
    name = "auniao"
    allowed_domains = ['auniao.pb.gov.br']
    start_urls = ['https://auniao.pb.gov.br/@@busca?SearchableText=barragem+mariana']

    BASE_URL = 'https://auniao.pb.gov.br/'

## Todo  Não está funcionando


    def parse(self, response):
      for article in response.css("dt"):

        link    = article.css("a::attr(href)").extract_first()
        # if link != "":
        #     conteudo  = response.follow(link, self.parse_article)
        conteudo = ""

        titulo  = response.css("a::text").extract_first()
        dataPublicacao = response.css("span.documentPublished").extract_first()


        notice = SigdesastrescrapyItem(titulo=titulo, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)
        yield notice        


      next_page = response.css('a.proximo::attr(href)').extract_first()
      if next_page is not None:
          yield response.follow(next_page, self.parse)
          
    def parse_article(self, response):
        conteudo = response.css("div.rnews:articleBody").getall()
        return conteudo
        

        

    
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