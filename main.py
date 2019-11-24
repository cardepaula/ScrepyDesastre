from bs4 import BeautifulSoup as bs
# import requests
import json, glob, sys
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

def ehvalido(objeto):
    palavas = ['mariana','desastre','vale','ambieltal','tragedia']

    for i in palavas:
        if i in objeto['descricao'].lower():
            return True
        if i in objeto['titulo'].lower():
            return True

    return False


def main():
    list_of_files = []
    list_of_files = list_files()
    request = RequestX()
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
                    response = request.post(objeto, "https://sigdesastre.herokuapp.com/noticias")
                    print("Valido:")
                    print(response)
                except:
                    print ('Algo deu errado')
                    print(response)




main()