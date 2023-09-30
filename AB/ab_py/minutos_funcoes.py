#3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

#entrada
def main() :
    minutos = int(input('Insira um valor em minutos:'))
    hor, min = calculo(minutos)
    saida(hor, min)

#process
def calculo(minutos) :
    hor = minutos // 60
    min = minutos % 60
    return hor, min

#saída
def saida(hor, min) :
    print('Isso corresponde a',hor,'horas e',min,'minutos')