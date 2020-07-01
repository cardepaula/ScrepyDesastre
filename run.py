# import schedule
import time
import os
import apiscrapy.em as em
import apiscrapy.bvsalud as bvsalud
import apiscrapy.scielo as scielo
# Functions setup


def call():
    os.system("scrapy crawl agu -o out/agu.json")
    os.system("scrapy crawl bloomberg -o out/bloomberg.json")
    # os.system("scrapy crawl conjur -o out/conjur.json") ## Robots.txt disallow
    os.system("scrapy crawl correiodoestadoonline -o out/correiodoestadoonline.json")
    os.system("scrapy crawl diariodoaco -o out/diariodoaco.json")
    os.system("scrapy crawl diariopopularmg -o out/diariopopularmg.json")
    os.system("scrapy crawl drd -o out/drd.json")
    os.system("scrapy crawl folhadocomercio -o out/folhadocomercio.json")
    os.system("scrapy crawl justificando -o out/justificando.json")
    os.system("scrapy crawl mpf -o out/mpf.json")
    os.system("scrapy crawl oolhar -o out/oolhar.json")
    os.system("scrapy crawl plox -o out/plox.json")
    os.system("scrapy crawl portalminas -o out/portalminas.json")
    os.system("scrapy crawl radargeral -o out/radargeral.json")
    os.system("scrapy crawl saudemg -o out/saudemg.json")
    os.system("scrapy crawl sitedelinhares -o out/sitedelinhares.json")
    os.system("scrapy crawl sonhoseguro -o out/sonhoseguro.json")

    em.run()  # extrai da API
    bvsalud.run()  # extrai do CSV
    scielo.run()  # extrai do CSV

    # envia noticias
    #os.system("python main.py")

    # remove arquivos
    #os.system('rm -r out/')


def fiocruz():
    os.system("wget https://bigdata-arquivos.icict.fiocruz.br/SIH/ETLSIH.zip")
    os.system('unzip ETLSIH.zip')
    os.system('cp -r ./home/dataiku/dss/exports/data ./out')


# Task scheduling
# After every 10mins geeks() is called.
# schedule.every(1).minutes.do(call)
# After every hour geeks() is called.
# schedule.every().hour.do(call)


# schedule.every(1).minutes.do(call)
# schedule.every(1).monday.do(fiocruz)

# print("funcionando")
# while True:
#     schedule.run_pending()
#     time.sleep(1)
call()
