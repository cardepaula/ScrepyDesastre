# coding=utf-8
import scrapy


class MaingSpider(scrapy.Spider):
    name = 'mpf'

    allowed_domains = ['www.mpf.mp.br']

    start_urls = [
        'http://www.mpf.mp.br/@@search?path=&SearchableText=desastre+mariana']

    def parse(self, response):

        for title in response.css('a.state-published'):
            link = article.css("a::attr(href)").extract_first()
            yield response.follow(self.BASE_URL+link, self.parse_article)

    def parse_article(self, response):

        link = response.url
        titulo = response.xpath(
            "//h2//text()").extract_first('')
        dataPublicacao = self.data_parse(
            response.xpath("//div[has-class('data')]/text()").extract_first())

        sep = ','
        conteudo = sep.join(response.xpath(
            '//div[has-class("noticia")]//p/text()').getall())

        cf = Fonte()
        fonte = cf.createFonte(self.name)
        midias = []
        grupoAcesso = cf.GRUPOACESSO
        descritores = []

        notice = SigdesastrescrapyItem(
            titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

        yield notice

    def data_parse(self, data):
        data = re.search(r'(\d+/\d+/\d+)', data)
        return data.group()
