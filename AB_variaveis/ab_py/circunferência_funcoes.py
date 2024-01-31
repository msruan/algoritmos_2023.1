#18. Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)

import math
#entrada
def main() :
    raio = float(input('Informe o valor do raio da circunferência:'))
    comp  = calculo(raio)
    saida(comp)

#process
def calculo(raio) :
    comp = raio * 3.14 * 2
    return comp

#saída
def saida(comp) :
    print('O comprimento da circunferência é',math.floor(comp))

main()