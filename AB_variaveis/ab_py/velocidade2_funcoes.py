#6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

import math
#entrada
def main() :
    km_h = float(input('Digite a velocidade em km/h:'))
    m_s = calculo(km_h)
    saida(m_s)

#proces
def calculo(km_h) :
    m_s = km_h / 3.6
    return m_s

#saída
def saida(m_s) :
    print('Essa velocidade corresponde a',math.floor(m_s),'m/s')

main()