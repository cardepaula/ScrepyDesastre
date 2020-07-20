
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import datetime
import csv
from contextlib import closing


GRUPOACESSO = {'id': 1, 'nome': 'todos', }

FONTE = {'nome': 'Biblioteca Virtual em Sa\u00fade',
         'link': 'https://bvsalud.org',
         "descricao": "Centro Latino-Americano e do Caribe de Informa\u00e7\u00e3o em Ci\u00eancias da Sa\u00fade",
         'tipoFonte': {
             'id': 2,
             'nome': "Ci\u00eancia"
         }}

LISTA_URL_CSV = [
    "https://pesquisa.bvsalud.org/portal/?output=csv&lang=pt&from=0&sort=&format=summary&count=-1&fb=&page=1&range_year_start=2015&range_year_end=2020&skfp=&index=tw&q=Desastre+rompimento",
    "https://pesquisa.bvsalud.org/portal/?output=csv&lang=pt&from=0&sort=&format=summary&count=-1&fb=&page=1&range_year_start=2015&range_year_end=2020&skfp=&index=tw&q=disaster+dam",
    "https://pesquisa.bvsalud.org/portal/?output=csv&lang=pt&from=0&sort=&format=summary&count=-1&fb=&page=1&range_year_start=2015&range_year_end=2020&skfp=&index=tw&q=disaster+samarco"
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
        'titulo': noticia[0],
        'link': noticia[11],
        'conteudo': '',
        'dataPublicacao': "%s/%s/%s" % (noticia[13][6:], noticia[13][4:6], noticia[13][0:4]),
        "descritores": ['Desastre', 'disaster', 'dam', 'rompimento', 'samarco'],
        'grupoAcesso': GRUPOACESSO,
        'fonte': FONTE
    }
    return nova


def salva_noticias_json(noticias):
    file_name = './out/bvsalud.json'
    with open(file_name, "w") as write_file:
        json.dump(noticias, write_file)


if __name__ == "__main__":
    main()
