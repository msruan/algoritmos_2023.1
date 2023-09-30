#Metabolismo basal ou Taxa metabólica basal é um método matemático, inexato, de calcular a quantidade calórica que o corpo necessita, em vinte e quatro horas, para manter-se nutrido durante o decorrer do dia.
#Fórmula da TMB para mulheres: TMB = 447,6 + (9,2 x peso) + (3,1 x altura) - (4,3 x idade)

import math
def main() :
    peso = float(input('Quanto você pesa? '))
    altura = float(input('Quantos centímetros você tem de altura? '))
    idade = int(input('Qual sua idade? '))
    tmb = calculo(peso,altura,idade)
    saida(tmb)
  
def calculo(peso, altura, idade) :
    tmb = 447.6 + (9.2 * peso) + (3.1 * (altura / 100)) - (4.3 * idade)
    return tmb
def saida(tmb) :
    print("O tmb é de",math.floor(tmb))

main()