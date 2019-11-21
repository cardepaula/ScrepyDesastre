from bs4 import BeautifulSoup as bs
import requests
import json

def main():
    dados = []

    page = requests.get("http://www.mpf.mp.br/atuacao-tematica/ccr4/@@updated_search?path=&b_start:int=0&SearchableText=desastre%20mariana")
    soup = bs(page.content, "html.parser")


    title = soup.find_all("a", class_="state-published")
    text = soup.find_all("div", class_="highlightedSearchTerm")

    # links = title.find_all('a').get('href')
    file = open('noticias.txt', 'w')
    for i in title:
        file.write(str(i)+'\n')
    file.close()
    # for j in range(len(title)):
    #     dicio = {
    #         "local": link[j].get_text(),
    #         "text": text[j].get_text(),
    #         "data": data[j].get_text(),
    #         "title": title[j].get_text()
    #     }
    #     dados.append(dicio)
    #
    # print(dados)

main()