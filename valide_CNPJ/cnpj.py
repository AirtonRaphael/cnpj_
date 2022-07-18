import re


def valida(cnpj):
    newCnpj = limpa(cnpj)
    newCnpj = novoCNPJ(newCnpj)
    return newCnpj
 
    
def limpa(cnpj):
    newCnpj = re.sub(r'[^0-9]','', cnpj)[:-2]
    return newCnpj


def novoCNPJ(newCnpj):
    def Digitos(newCnpj):
        calc = list(range(5, 1, -1)) + list(range(9, 1, -1))
        d1 = 11 - ((sum(map(lambda x,y: int(x)*int(y), newCnpj, calc))) % 11)
        if d1 > 9:
            d1 = 0 
        calc.insert(0, '6')
        newCnpj = newCnpj+str(d1)
        d2 = 11 - ((sum(map(lambda x,y: int(x)*int(y), newCnpj, calc))) % 11)
        if d2 > 9:
            d2 = 0
        newCnpj = newCnpj+str(d2)
        return newCnpj


    return Digitos(newCnpj)
