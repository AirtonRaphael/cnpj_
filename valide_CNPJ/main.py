#Valida CNPJ
import cnpj
import re

valide = '40.688.135/0001-61'
newCnpj = cnpj.valida(valide)
Validado = re.sub(r'[^ 0-9]','',valide)
if Validado == newCnpj:
    print(f'Cnpj: {valide} é valido')
else:
    print(f'Cnpj: {valide} não é valido')