# import requests
import json
import glob
import sys
import os
from requestx.RequestX import RequestX
PATH = "./out/"


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


def main():
    list_of_files = []
    list_of_files = list_files()
    request = RequestX()
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
                response = ""
                try:
                    response = request.post(
                        objeto, "https://sigdesastre.herokuapp.com/noticias")
                    print("Valido:")
                    print(response)
                except:
                    print('Algo deu errado')
                    print(response)

    print("finish push")


main()
