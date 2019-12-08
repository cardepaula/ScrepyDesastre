# coding=utf-8
import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem


class MpfSpider(scrapy.Spider):
    name = "mpf"
    allowed_domains = ['mpf.mp.br']
    start_urls = ['http://www.mpf.mp.br/@@updated_search?path=&b_start:int=0&SearchableText=desastre%20mariana']
## não está funcionando
