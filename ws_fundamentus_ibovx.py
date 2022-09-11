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
Fiis = [
    'CACR11'
,'BPFF11'
,'AFHI11'
,'ALZR11'
,'ARCT11'
,'ARRI11'
,'AIEC11'
,'BARI11'
,'BBPO11'
,'BCFF11'
,'BRCR11'
,'BCIA11'
,'BCRI11'
,'BLMR11'
,'BLMG11'
,'BRCO11'
,'BTAL11'
,'BTCR11'
,'BTRA11'
,'BTLG11'
,'CPFF11'
,'CPTS11'
,'HGCR11'
,'HGFF11'
,'HGLG11'
,'HGRU11'
,'CARE11'
,'DEVA11'
,'FEXC11'
,'VRTA11'
,'GTWR11'
,'GGRC11'
,'GALG11'
,'HABT11'
,'HCTR11'
,'HGBS11'
,'HGRE11'
,'HSAF11'
,'HSLG11'
,'HSML11'
,'HFOF11'
,'FIIB11'
,'IRDM11'
,'JSRE11'
,'KISU11'
,'KNRI11'
,'KNHY11'
,'KNIP11'
,'KNCR11'
,'KNSC11'
,'KFOF11'
,'NSLU11'
,'MALL11'
,'MCCI11'
,'MCHF11'
,'MXRF11'
,'MFII11'
,'MGFF11'
,'MORE11'
,'NCHB11'
,'OUJP11'
,'PATL11'
,'PLCR11'
,'PORD11'
,'QAGR11'
,'RBRL11'
,'RBRY11'
,'RBRP11'
,'RBRF11'
,'RBRR11'
,'RECR11'
,'RECT11'
,'RBFF11'
,'RCRB11'
,'RBVA11'
,'RZAK11'
,'RZTR11'
,'SADI11'
,'SARE11'
,'SDIL11'
,'SPTW11'
,'SNCI11'
,'SNFF11'
,'TGAR11'
,'TORD11'
,'TRXF11'
,'URPR11'
,'VGHF11'
,'VGIP11'
,'VGIR11'
,'CVBI11'
,'LVBI11'
,'PVBI11'
,'RVBI11'
,'VCJR11'
,'VSLH11'
,'VIFI11'
,'VIUR11'
,'VILG11'
,'VINO11'
,'VISC11'
,'VTLT11'
,'XPCI11'
,'XPIN11'
,'XPLG11'
,'XPML11'
,'XPPR11'
,'XPSF11'
]

#---

indicadores = fdts(Fiis)
indicadores.outContentCsv()
#indicadores.printContentScreen()
#indicadores.printContentScreen(addIbvx=1)
#indicadores.printContentScreen(addIbvx=1, qtdpregoes='10')
#--


