import pandas as pd
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
        
        pasta_destino = '.'
        if('destino' in kwargs and kwargs['destino'] is not None):
            pasta_destino = kwargs['destino'].strip()

        nome = 'novo_arquivo'
        if('nome' in kwargs and kwargs['nome'] is not None):
            nome = kwargs['nome'].strip()

        caminho_nome_final = pasta_destino+'/'+nome+'.csv'
        
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
            cotacao = tables[0].find_all('td', attrs={'class':'data destaque w3'})[0].find('span').text
            segmento = tables[0].find_all('tr')[3].find_all('td', attrs={'class':'data'})[0].find('span').text
            ffoyield = tables[2].find_all('tr')[1].find_all('td', attrs={'class':'data'})[1].find('span').text
            divyield = tables[2].find_all('tr')[2].find_all('td', attrs={'class':'data'})[1].find('span').text
            ppv = tables[2].find_all('tr')[3].find_all('td', attrs={'class':'data'})[1].find('span').text
            vpcota = tables[2].find_all('tr')[3].find_all('td', attrs={'class':'data'})[2].find('span').text

            print(f'Lendo em fundamentus - ({ctFundo} de {ttFundos}) FUNDO: {fii} ...')
            dados.append({'fundo':fii,'segmento':segmento, 'cotacao':cotacao, 'ffoyield':ffoyield, 'divyield':divyield, 'ppv':ppv, 'vpcota':vpcota})
            ctFundo = ctFundo+1
        
        print(f'Criando o arquivo: {caminho_nome_final}')
        
        try:
            df = pd.DataFrame(dados)
            df.to_csv(caminho_nome_final, sep=';', index=False, encoding='iso-8859-1')
            print(f'Arquivo {caminho_nome_final} criado com sucesso!\n')
        except:
            print(f'Opsss... ocorreu um erro na geração do arquivo {caminho_nome_final}! #sorry\n')
            