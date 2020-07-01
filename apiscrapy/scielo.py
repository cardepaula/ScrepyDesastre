

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import datetime
import csv
from contextlib import closing

GRUPOACESSO = {'id': 1, 'nome': 'todos', }

FONTE = {'nome': "scielo",
         'link': "https://search.scielo.org/",
         'descricao': "scielo",
         'tipoFonte': {
             'id': 2,
             'nome': "Ciência"
         }}

LISTA_URL_CSV = [
    'https://search.scielo.org/?q=disaster+samarco&lang=pt&count=-1&from=0&output=csv&sort=&format=summary&fb=&page=1',
    'https://search.scielo.org/?q=desastre+samarco&lang=pt&count=-1&from=0&output=csv&sort=&format=summary&fb=&page=1',
    'https://search.scielo.org/?q=Desastre+rompimento&lang=pt&count=15&from=0&output=csv&sort=&format=summary&fb=&page=1'
]


def run():
    main()


def main():
    noticias = []
    for i in LISTA_URL_CSV:
        noticias = noticias + extrai_noticia(i)
    salva_noticias_json(noticias)


def extrai_noticia(url):
    noticias_list = []
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        for row in list(cr)[1:]:
            noticias_list.append(cria_noticia(row))
    return noticias_list


def cria_noticia(noticia):

    nova = {
        'titulo': noticia[1],
        'link': noticia[7],
        'conteudo': '',
        'dataPublicacao': '01-01-'+noticia[6],
        "descritores": ['Desastre', 'rompimento', 'samarco'],
        'grupoAcesso': GRUPOACESSO,
        'fonte': FONTE
    }
    return nova


def salva_noticias_json(noticias):
    file_name = './out/scielo.json'
    with open(file_name, "w") as write_file:
        json.dump(noticias, write_file)


if __name__ == "__main__":
    main()
