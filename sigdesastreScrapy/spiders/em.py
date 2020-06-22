import scrapy
from sigdesastreScrapy.items import SigdesastrescrapyItem
from .createfonte import Fonte


class MaingSpider(scrapy.Spider):
    name = "em"
    allowed_domains = ['www.em.com.br']
    start_urls = [
        'https://www.em.com.br/busca/barragem%20fund%C3%A3o?json=63c055b-c8a7-4010-92c6-01803d6e752e']

    BASE_URL = 'www.em.com.br'
    # TODO Fazer

    def parse(self, response):
        # link = response.xpath("//arr[@name='ur']//text()").extract()
        JsonRequest(
            'https://www.em.com.br/busca/barragem%20fund%C3%A3o?json=63c055b-c8a7-4010-92c6-01803d6e752e')
        print()
        # cf = Fonte()
        # fonte = cf.createFonte(self.name)
        # midias = []
        # grupoAcesso = cf.GRUPOACESSO
        # descritores = []
        # notice = SigdesastrescrapyItem(
        #     titulo=titulo, descritores=descritores, midias=midias, fonte=fonte, grupoAcesso=grupoAcesso, conteudo=conteudo, link=link, dataPublicacao=dataPublicacao)

    def doc_parse(self, response):
        pass

    def data_parse(self, data):
        texto = ""
        try:

            texto = "01-%s-%s" % (data[4:], data[:4])

        except:

            print("erro ao converter data")

        return texto
