import requests as rq
from bs4 import BeautifulSoup
#---
from servicos.conversor import Conversor as conv
#---

class Ibovx:

    def __init__(self, Fiis) -> None:
        self.fiis = Fiis
        self.header = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }
        
    def printContentScreen(self, qtdpregoes = '5'):
        for fii in self.fiis:
            #site IBOVX 
            target_url_hist = 'https://www.ibovx.com.br/historico-papeis-bovespa.aspx?papel='+fii+'&qtdpregoes='+qtdpregoes
            target_page_hist = rq.get( target_url_hist, headers=self.header )
            print(f'{fii} - HISTÓRICO ({qtdpregoes}) NEGOCIAÇÕES NA B3: IBOVX')
            print('-'*15)

            if(target_page_hist.status_code!=200):
                print(f'Ocorreu um erro na requisição da página: {target_page_hist}')
                break

            try:
                page = BeautifulSoup(target_page_hist.text, 'html.parser')
                trs = page.find_all('table')[1].find_all('tr')
                cont = 0
                for v in trs:
                    try:
                        td_data = v.find_all('td')[0].text
                        td_variacao_perc = v.find_all('td')[1].text
                        td_variacao = v.find_all('td')[2].text
                        td_cotacao = v.find_all('td')[3].text
                        td_abertura = v.find_all('td')[4].text
                        td_min = v.find_all('td')[5].text
                        td_max = v.find_all('td')[6].text
                        td_vol = v.find_all('td')[7].text
                        td_num_negocios = v.find_all('td')[8].text

                        if cont>0:
                            td_variacao_perc = conv.strToFloat( conv.comaToPoint( td_variacao_perc ) )
                            td_variacao = conv.strToFloat( conv.comaToPoint( td_variacao ) )
                            td_cotacao = conv.strToFloat( conv.comaToPoint( td_cotacao ) )
                            td_abertura = conv.strToFloat( conv.comaToPoint( td_abertura ) )
                            td_min = conv.strToFloat( conv.comaToPoint( td_min ) )
                            td_max = conv.strToFloat( conv.comaToPoint( td_max ) )
                          
                        print(f'{td_data} | {td_variacao_perc} | {td_variacao} | {td_cotacao} | {td_abertura} | {td_min} | {td_max} | {td_vol} | {td_num_negocios}')
                    except IndexError: #não exibe banner de propaganda
                        pass
                    
                    cont = cont + 1   
                    if cont > int(qtdpregoes):
                        break

                print('\n-------------\n')

            except Exception as e: #BeautifulSoup - ibovx
                print(f'{e}')
