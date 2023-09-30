#Metabolismo basal ou Taxa metabólica basal é um método matemático, inexato, de calcular a quantidade calórica que o corpo necessita, em vinte e quatro horas, para manter-se nutrido durante o decorrer do dia.
#Fórmula da TMB para homens: TMB = 88,36 + (13,4 x peso) + (4,8 x altura) - (5,7 x idade)

import math
def main() :
    peso = float(input('Qual seu peso? '))
    altura = float(input('Qual sua altura em centímetros? '))
    idade = int(input('Quantos anos você tem? '))
    tmb = calculo(peso,altura,idade)
    saida(tmb)
  
def calculo(peso, altura, idade) :
    tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    return tmb
def saida(tmb) :
    print("O tmb é de",math.floor(tmb))

main()