#Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles

#entrada
def main() :
    x1 = float(input('Qual a coordenadada x do primeiro ponto? '))
    y1 = float(input("Qual a coordenadada y do primeiro ponto? "))
    x2 = float(input('Qual a coordenadada x do primeiro ponto? '))
    y2 = float(input('Digite o segundo número: '))
    resul = calculo(x1, y1, x2, y2)
    saida(resul)

#process
def calculo(x1, y1, x2, y2) :
    resul = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return resul

#saída
def saida(resul) :
    print('A distância entre os pontos é:',resul)

main()