from tokenize import String

class Conversor:

    def __init__(self) -> None:
        pass
        
    def comaToPoint(str) -> String:
        return str.replace(',','.')

    def strToFloat(str,kza=2) -> float:
        if type(kza) != int:
            print(f'kza="{kza}" tem q ser inteiro!')
            return 
            
        # se existir % na última posição da string
        if str.count('%') > 0 and str.find('%')==len(str)-1:
            str = str[:-1]

        return round(float(str),kza)

    