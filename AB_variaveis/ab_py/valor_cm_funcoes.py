#24. Leia um valor em m, calcule e escreva o equivalente em cm.

print('Olá, tudo bem?')
#entrada
def main() :
    metro = float(input('Digite um valor em metros:'))
    cen = calculo(metro)
    saida(cen)

#proces 
def calculo(metro) :
    cen = metro * 100
    return cen

#saída
def saida(cen) :
    print('Isso corresponde a',cen,'centímetros!')

main()