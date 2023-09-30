#30. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

#entrada
def main() :
    min = int(input('Digite o número de minutos: '))
    dias, horas, minutos = calculo(min)
    saida(dias, horas, minutos)

#proces
def calculo(min) :
    dias = min // 1440
    horas = (min % 1440) // 60
    minutos = (min % 1440) % 60
    return dias, horas, minutos

#saída
def saida(dias, horas, minutos) :
    print ('Isso é igual a',dias,'dias,',horas,'horas e',minutos,'minutos!')

main()