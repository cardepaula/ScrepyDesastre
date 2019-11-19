import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class SaudemgSpider(scrapy.Spider):
    name = "saudemg"
    allowed_domains = ['saude.mg.gov.br']
    start_urls = ['http://saude.mg.gov.br/component/search/?all=desastre+mariana&exact=&any=&none=&created=&modified=&area=all']

    def start_requests(self):
        urls = [
            'http://saude.mg.gov.br/component/search/?all=desastre+mariana&exact=&any=&none=&created=&modified=&area=all'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for card in response.css('card.masonry-brick'):
            yield response.follow(card, self.parse_article)

    def parse_article(self, response):
        link = response.css('h2.title a ::attr(href)').extract_first()
        title = response.css('h2.title a ::text').extract_first()
        author = ''
        # text = "".join(response.css('div.entry ::text').extract()).strip()
        text = ""

        item = SigdesastrescrapyItem(link=link, author=author, title=title, text=text)
        yield item