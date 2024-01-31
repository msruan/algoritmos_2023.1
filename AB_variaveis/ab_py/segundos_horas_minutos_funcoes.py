#27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

#entrada
def main() :
    seg = int(input('Quantos segundos? '))
    hor, min, seconds = calculo(seg)
    saida(hor, min, seconds)

#proces
def calculo(seg) :
    hor = seg // 3600
    min = seg // 60 - (hor * 60)
    seconds = seg % 60
    return hor, min, seconds

#saída
def saida(hor, min, seconds) :
    print("Isso corresponde a",hor,'horas,',min,'minutos e',seconds,'segundos')

main()