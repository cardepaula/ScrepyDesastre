class Fonte():

    FONTES = {
        "agu": {
            "nome": "Advocacia Geral da União",
            "url": "https://www.agu.gov.br",
            "idfonte": 1,
            "descricao": "Advocacia Geral da União"
        },
        "bloomberg": {
            "nome": "Serviço Bloomberg Professional",
            "url": "https://www.bloomberg.com.br/",
            "idfonte": 0,
            "descricao": "Serviço Bloomberg Professional"
        },
        "bvsalud": {
            "nome": 'Biblioteca Virtual em Saúde',
            "url": 'https://bvsalud.org',
            "idfonte": 2,
            "descricao": 'Centro Latino-Americano e do Caribe de Informação em Ciências da Saúde'
        },
        "conjur": {
            "nome": 'ConJur',
            "url": 'https://www.conjur.com.br',
            "idfonte": 6,
            "descricao": 'revista eletrônica Consultor Jurídico'
        },
        "correiodoestadoonline": {
            "nome": "Correio do Estado Online",
            "url": "http://www.correiodoestadoonline.com.br",
            "idfonte": 5,
            "descricao": "Correio do Estado Online"
        },
        "diariodoaco": {
            "nome": "Diário do Aço",
            "url": 'https://www.diariodoaco.com.br',
            "idfonte": 5,
            "descricao": 'Diário do Aço'
        },
        "diariopopularmg": {
            "nome": "Diário Popular MG",
            "url": "http://www.diariopopularmg.com.br",
            "idfonte": 5,
            "descricao": "Diário Popular MG"
        },
        "drd": {
            "nome": "DRD News",
            "url": "https://drd.com.br/",
            "idfonte": 5,
            "descricao": "DRD News"
        },
        "folhadocomercio": {
            "nome": "Folha do Comércio",
            "url": "http://www.folhadocomercio.com.br",
            "idfonte": 5,
            "descricao": "Folha do Comércio"
        },
        "justificando": {
            "nome": "Justificando",
            "url": 'http://www.justificando.com',
            "idfonte": 6,
            "descricao": "Justificando"
        },
        "mpf": {
            "nome": "",
            "url": "",
            "idfonte": 0,
            "descricao": ""
        },
        "oolhar": {
            "nome": "O Olhar",
            "url": "https://oolhar.com.br",
            "idfonte": 5,
            "descricao": "O Olhar"
        },
        "plox": {
            "nome": "Portal Plox",
            "url": "https://plox.com.br",
            "idfonte": 5,
            "descricao": "Portal Plox"
        },
        "portalminas": {
            "nome": "Portal Minas",
            "url": "https://www.portalminas.com/",
            "idfonte": 5,
            "descricao": "Portal Minas"
        },
        "radargeral": {
            "nome": "Radar Geral",
            "url": "https://radargeral.com/",
            "idfonte": 5,
            "descricao": "Radar Geral"
        },
        "saudemg": {
            "nome": "Saude MG",
            "url": "http://saude.mg.gov.br",
            "idfonte": 1,
            "descricao": "Saude MG"
        },
        "scielo": {
            "nome": "scielo",
            "url": "https://search.scielo.org/",
            "idfonte": 2,
            "descricao": "scielo"
        },
        "sitedelinhares": {
            "nome": 'Site de Linhares',
            "url": 'https://www.sitedelinhares.com.br/',
            "idfonte": 1,
            "descricao": 'Site de Linhares'
        },
        "sonhoseguro": {
            "nome": "Sonho Seguro",
            "url": "https://www.sonhoseguro.com.br/",
            "idfonte": 6,
            "descricao": "Sonho Seguro"
        }
    }
    TIPOFONTE = {
        2: "Ciência",
        3: "Associações",
        4: "Midias Sociais",
        5: "Fontes Noticiosas",
        6: "Iniciativa Privada",
        1: "Fontes Oficiais"
    }
    GRUPOACESSO = {'id': 1, 'nome': 'todos', }

    def createFonte(self, name):

        nome = self.FONTES[name]["nome"]
        link = self.FONTES[name]["url"]
        descricao = self.FONTES[name]["descricao"]
        idFonte = self.FONTES[name]["idfonte"]
        nomeFonte = self.TIPOFONTE[idFonte]

        newFonte = {'nome': nome,
                    'link': link,
                    'descricao': descricao,
                    'tipoFonte': {
                        'id': idFonte,
                        'nome': nomeFonte
                    }}
        return newFonte
