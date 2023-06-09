#Leia um número, calcule e escreva seu fatorial.
from funcao import show, obter_inteiro_positivo
def main():
    a_fatoriar = obter_inteiro_positivo()
    fatorial = obter_fatorial(a_fatoriar)
    show(f'{a_fatoriar}! é igual a {fatorial}.')
def obter_fatorial(numero):
    multiplicador = 1
    for i in range(1,numero+1):
        multiplicador *= i
    return multiplicador
main()