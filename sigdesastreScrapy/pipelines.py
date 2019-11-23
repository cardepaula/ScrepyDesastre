# -*- coding: utf-8 -*-
import json
import requests
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SigdesastrescrapyPipeline(object):

    # def process_item(self, item, spider):
    #     url = 'https://sigdesastre.herokuapp.com/noticias'
    #     headers = {'content-type': 'application/json'}
    #     x = requests.post(url, data=json.dumps(item), headers=headers)


