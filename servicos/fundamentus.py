import pandas as pd
import csv
import requests as rq
from bs4 import BeautifulSoup
#---
from servicos.ibovx import Ibovx as ibovx
from servicos.conversor import Conversor as conv
#---

class Fundamentus:

    def __init__(self, Fiis) -> None:
        self.fiis = Fiis
        self.header = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
        

    def printContentScreen(self, addIbvx = 0, **kwargs):
        for fii in self.fiis:
            #site FUNDAMENTUS 
            target_url = 'https://www.fundamentus.com.br/detalhes.php?papel='+fii
            target_page = rq.get( target_url, headers=self.header )

            if(target_page.status_code!=200):
                print(f'Ocorreu um erro na requisição da página: {target_page}')
                break

            page = BeautifulSoup(target_page.text, 'html.parser')
            tables = page.find_all('table')
            cotacao = conv.strToFloat( conv.comaToPoint( tables[0].find_all('td', attrs={'class':'data destaque w3'})[0].find('span').text ) )
            segmento = tables[0].find_all('tr')[3].find_all('td', attrs={'class':'data'})[0].find('span').text
            ffoyield = conv.strToFloat( conv.comaToPoint( tables[2].find_all('tr')[1].find_all('td', attrs={'class':'data'})[1].find('span').text ) )
            divyield = conv.strToFloat( conv.comaToPoint( tables[2].find_all('tr')[2].find_all('td', attrs={'class':'data'})[1].find('span').text ) )
            ppv = conv.strToFloat( conv.comaToPoint( tables[2].find_all('tr')[3].find_all('td', attrs={'class':'data'})[1].find('span').text ) )
            vpcota = conv.strToFloat( conv.comaToPoint( tables[2].find_all('tr')[3].find_all('td', attrs={'class':'data'})[2].find('span').text ) )
            
            print(f'FUNDO: {fii}\nSegmento: {segmento}\nCotação: {cotacao} | FFO Yield(%): {ffoyield} | DIV. Yield(%): {divyield} | P/PV: {ppv} | VP/Cota: {vpcota}\n')
            
            # se solicita anexar ibovx
            if addIbvx!=0:
                # verifica se a chave qtdpregoes foi solicitada
                # senão foi, o padrão é 5 últimos pregões
                try:
                    # chamando o serviço Ibovx
                    pregoes = ibovx([fii])
                    pregoes.printContentScreen(kwargs['qtdpregoes'])
                except KeyError:
                    pregoes.printContentScreen()


    def outContentCsv(self, addIbvx = 0, **kwargs):
        dados = []
        ttFundos = len(self.fiis)
        ctFundo = 1
        for fii in self.fiis:
            #site FUNDAMENTUS 
            target_url = 'https://www.fundamentus.com.br/detalhes.php?papel='+fii
            target_page = rq.get( target_url, headers=self.header )

            if(target_page.status_code!=200):
                print(f'Ocorreu um erro na requisição da página: {target_page}')
                break

            page = BeautifulSoup(target_page.text, 'html.parser')
            tables = page.find_all('table')
            cotacao = conv.strToFloat( conv.comaToPoint( tables[0].find_all('td', attrs={'class':'data destaque w3'})[0].find('span').text ) )
            segmento = tables[0].find_all('tr')[3].find_all('td', attrs={'class':'data'})[0].find('span').text
            ffoyield = conv.strToFloat( conv.comaToPoint( tables[2].find_all('tr')[1].find_all('td', attrs={'class':'data'})[1].find('span').text ) )
            divyield = conv.strToFloat( conv.comaToPoint( tables[2].find_all('tr')[2].find_all('td', attrs={'class':'data'})[1].find('span').text ) )
            ppv = conv.strToFloat( conv.comaToPoint( tables[2].find_all('tr')[3].find_all('td', attrs={'class':'data'})[1].find('span').text ) )
            vpcota = conv.strToFloat( conv.comaToPoint( tables[2].find_all('tr')[3].find_all('td', attrs={'class':'data'})[2].find('span').text ) )

            print(f'Lendo em fundamentus - ({ctFundo} de {ttFundos}) FUNDO: {fii}...\n')
            dados.append({'fundo':fii,'segmento':segmento, 'cotacao':cotacao, 'ffoyield':ffoyield, 'divyield':divyield, 'ppv':ppv, 'vpcota':vpcota})
            ctFundo = ctFundo+1
        
        df = pd.DataFrame(dados)
        print(df)
        #df_out = pd.to_csv(dados)
            