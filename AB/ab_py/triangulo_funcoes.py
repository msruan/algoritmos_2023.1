#15. Leia o valor da base e altura de um triângulo, calcule e escreva sua área. (área=(base * altura)/2)

#entrada
def main() :
    base = float(input('Insira o comprimento da base do triângulo:'))
    altura = float(input('Digite a altura:'))
    area = calculo(base, altura)
    saida(area)

#proces
def calculo(base, altura) :
    area = (base * altura) / 2
    return area

#saída
def saida(area) :
    print('A área do triângulo é',area)

main()