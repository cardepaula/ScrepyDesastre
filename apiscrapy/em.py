
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests as request
import json
import datetime

GRUPOACESSO = {'id': 1, 'nome': 'todos', }

FONTE = {'nome': 'Estado de Minas',
         'link': 'https://www.em.com.br/',
         'descricao': 'Estado de Minas',
         'tipoFonte': {
             'id': 6,
             'nome': "Fontes Noticiosas"
         }}


def run():
    main()


def main():
    url = 'https://www.em.com.br/busca/barragem%20fund%C3%A3o?json=63c055b-c8a7-4010-92c6-01803d6e752e'
    headers = {'content-type': 'application/json'}
    response = request.get(url, headers=headers)

    resp = json.loads(response.content)

    noticias = proxima_pagina(resp['next'])

    print('salvando')
    salva_noticias_json(noticias)
    print('salvo som sucesso!')


def proxima_pagina(url):
    headers = {'content-type': 'application/json'}
    response = request.get(url, headers=headers)
    resp = json.loads(response.content)
    noticias = []
    if 'next' in resp:
        print(resp['next'])
        noticias = proxima_pagina(resp['next'])
    return noticias + extrai_noticia(resp['news'])


def extrai_noticia(listaNoticia):
    noticias = []
    for noticia in listaNoticia:
        noticiaf = cria_noticia(noticia)
        noticias.append(noticiaf)
    return noticias


def cria_noticia(noticia):
    nova = {
        'titulo': noticia['title'],
        'link': noticia['url'],
        'conteudo': noticia['description'] if noticia['description'] else '',
        'dataPublicacao': noticia['date_time'],
        "descritores": ['fundão', 'barragem'],
        'grupoAcesso': GRUPOACESSO,
        'fonte': FONTE
    }
    return nova


def salva_noticias_json(noticias):
    file_name = './out/em.json'
    with open(file_name, "w") as write_file:
        json.dump(noticias, write_file)


if __name__ == "__main__":
    main()
