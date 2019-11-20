import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem

class MpfSpider(scrapy.Spider):
    name = "mpf"
    allowed_domains = ['mpf.mp.br']
    start_urls = ['http://www.mpf.mp.br/@@updated_search?path=&b_start:int=0&SearchableText=desastre%0mariana']

    def parse(self, response):
        try:
            for article in response.css('a state-published'):
                link = article.css('div.texts h2 a::attr(href)').extract_first()
                yield response.follow(link, self.parse_article)

            next_page = response.css('a#mais::attr(href)').extract_first()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
        except Exception:
            print("Ocorreu erro no Parse")

    def parse_article(self, response):
        link = response.url
        title = response.css('title ::text').extract_first()
        author = response.css('span.author ::text').extract_first()
        # text = "".join(response.css('div.entry ::text').extract()).strip()
        text = ""

        item = TecnoblogItem(link=link, author=author, title=title, text=text)

        yield item