#!/usr/bin/env python
# -*-

import json
import glob
import sys
import os
import requests as request
import datetime
PATH = "./out/"

api_url =  os.getenv("API_URL")  # "http://localhost:3000/noticias"

def list_files():
    files = []
    try:
        files_path = glob.glob(PATH + "*.json")
        files_path.sort()
        for f in files_path:
            if sys.platform == "win32":
                files.append(f.split("\\")[-1])
            else:
                files.append(f.split("/")[-1])
        return files
    except Exception as err:
        print(err)
        return []


def transformadata(objeto):
    if "dataPublicacao" in objeto:
        data = datetime.datetime.strptime(objeto["dataPublicacao"], '%d-%m-%Y')
        objeto["dataPublicacao"] = "%s-%s-%s" % (
            data.year, data.month, data.day)

    if "dataCriacao" in objeto:
        data = datetime.datetime.strptime(objeto["dataCriacao"], '%d-%m-%Y')
        objeto["dataCriacao"] = "%s-%s-%s" % (data.year, data.month, data.day)

    if "dataAtualizacao" in objeto:
        data = datetime.datetime.strptime(
            objeto["dataAtualizacao"], '%d-%m-%Y')
        objeto["dataAtualizacao"] = "%s-%s-%s" % (
            data.year, data.month, data.day)

    return objeto


def e_valido(noticia):
    descritores = ['mariana', 'samarco', 'vale', 'rio doce',
                   'disaster', 'desastre', 'dam', 'rompimento', 'tragédia']
    conteudo = '%s %s' % (noticia['titulo'].lower(),
                          noticia['conteudo'].lower())

    for descritor in descritores:
        if descritor in conteudo:
            return True

    return False


def main():
    list_of_files = []
    list_of_files = list_files()
    headers = {'content-type': 'application/json'}
    print("start push")
    for file in list_of_files:
        with open(PATH+file) as json_file:
            try:
                data = json.load(json_file)
            except:
                data = []
                print("erro ao carregar json")
            print(file)
            for objeto in data:
                # objeto = transformadata(objeto)
                response = ""
                try:
                    # "" #
                    url = api_url
                    response = request.post(
                        url, data=json.dumps(objeto), headers=headers)

                    if 500 in response:
                        raise Exception("erro 500")
                    print(objeto["titulo"])
                    print(response)
                except Exception as erro:
                    print('Algo deu errado %s' % erro)
                    print(response)

    print("finish push")


main()
