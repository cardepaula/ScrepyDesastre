import schedule
import time
import os

# Functions setup


def call():
    os.system("scrapy crawl agu -o out/agu.json")
    os.system("scrapy crawl bloomberg -o out/bloomberg.json")
    os.system("scrapy crawl bloomberg -o out/bloomberg.json")
    os.system("scrapy crawl bvsalud -o out/bvsalud.json")
    os.system("scrapy crawl conjur -o out/conjur.json")
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
    os.system("scrapy crawl scielo -o out/scielo.json")
    os.system("scrapy crawl sitedelinhares -o out/sitedelinhares.json")
    os.system("scrapy crawl sonhoseguro -o out/sonhoseguro.json")

    os.system("python main.py")


# Task scheduling
# After every 10mins geeks() is called.
# schedule.every(1).minutes.do(call)
# After every hour geeks() is called.
# schedule.every().hour.do(call)
schedule.every(1).minutes.do(call)


print("funcionando")
while True:
    schedule.run_pending()
    time.sleep(1)
