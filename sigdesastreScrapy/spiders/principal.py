import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem


class SaudemgSpider(scrapy.Spider):
    name = "saudemg"
    allowed_domains = ['saude.mg.gov.br']
    start_urls = ['http://saude.mg.gov.br']

    def parse(self, response):
        for quote in response.css('a ::attr(href)'):
            yield {
                'link': quote.css('a ::attr(href)').extract_first() ,
                'corpo': quote.css('body').extract_first()
            }
