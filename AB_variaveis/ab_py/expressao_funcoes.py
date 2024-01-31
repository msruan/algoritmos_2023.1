#39: Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:

#entrada
def main() :
    a = int(input('Qual o primeiro número? '))
    b = int(input('Qual o segundo? '))
    c = int(input('Qual é o terceiro número? '))
    d = calculo(a,b,c)
    saida(d)

#process
def calculo(a,b,c) :
    r = (a + b) ** 2
    s = (b + c) ** 2
    d = (r + s) / 2
    return d

#saída
def saida(d) :
    print("O resultado é",d)

main()