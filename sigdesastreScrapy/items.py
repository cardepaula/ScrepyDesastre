# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SigdesastrescrapyItem(scrapy.Item):
    link = scrapy.Field()
    descricao = scrapy.Field()
    dataPublicacao = scrapy.Field()
    titulo = scrapy.Field()
    conteudo = scrapy.Field()
    dataCriacao = scrapy.Field()
    dataAtualizacao = scrapy.Field()
    fonte = scrapy.Field()
    midias = scrapy.Field()
    grupoAcesso = scrapy.Field()
    descritores = scrapy.Field()
