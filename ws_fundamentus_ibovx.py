'''
Autor: Adair J. Rossatto Commodo
Licença: MIT
Objetivo: 
    - Obter INDICADORES de Fundos de Investimentos Imobiliários (Fii's) do site Fundamentos (https://www.fundamentus.com.br)
    - Obter HISTÓRICO de negociações na B3 através do site IBOVX (https://www.ibovx.com.br)
    - Exibir na tela INFORMAÇÕES AGREGADAS.
Dependencias:
    - Requests: pip install requests
    - BS4 (BeautifulSoup): pip install bs4
    - Módulos Próprios (diretorio servicos): 
        --> fundamentus.py
        --> ibovx.py
        --> conversor.py
'''

from servicos.fundamentus import Fundamentus as fdts
#---

# Entre com o código do FII
Fiis = ['VGHF11','RZTR11']
#---

indicadores = fdts(Fiis)
#indicadores.printContentScreen()
indicadores.printContentScreen(addIbvx=1)
#indicadores.printContentScreen(addIbvx=1, qtdpregoes='10')
#--


