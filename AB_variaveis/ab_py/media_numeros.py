#34. Leia 3 números, calcule e escreva a média dos números.

import math
#entrada
prim = float(input("Digite o primeiro número: "))
seg = float(input('Qual o segundo número? '))
ter = float(input('Insira o terceiro: '))

#proces
media = (prim + seg + ter) / 3

#saída
print('A média desses números é aproximadamente',math.floor(media))