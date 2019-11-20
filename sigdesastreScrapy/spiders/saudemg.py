import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class SaudemgSpider(scrapy.Spider):
    name = "saudemg"
    allowed_domains = ['saude.mg.gov.br']
    start_urls = ['http://saude.mg.gov.br/component/search/?all=desastre+mariana&exact=&any=&none=&created=&modified=&area=all']

    def parse(self, response):
        for quote in response.css('div.card'):
            yield {
                'link': quote.css('h2.title a ::attr(href)').extract_first(),
                'text': quote.css('div.description::text').extract_first(),
                'data': quote.css('span.date ::text').extract_first(),
                'title': quote.css('h2.title a ::text').extract_first()
            }