#Escreva a tabuada dos números de 1 a 10 dado um limite.
from funcao import show, obter_inteiro_positivo
def main():
    limite_inferior = obter_inteiro_positivo('Digite o limite inferior: ')
    limite_superior = obter_inteiro_positivo('Digite o limite superior: ')
    if limite_superior < limite_inferior:
        show("Por favor, tenha certeza de que o limite superior é maior que o inferior!")
        return main()
    tabuada(limite_inferior,limite_superior)

'''recebe dois números como limites, e calcula a tabuada de seu intervalo
(incluindo os números fornecidos)'''
def tabuada(limite_inferior,limite_superior):

    show(f'\nTABUADA de {limite_inferior} a {limite_superior}:\n')

    show(50*'=')
    show('\nADIÇÃO\n')
    somador_atual = limite_inferior
    while somador_atual <= limite_superior:
        operacao_um_a_dez('A',somador_atual)
        somador_atual += 1

    show(50*'=')
    show(f'\nSUBTRAÇÃO')
    diminuendo_atual = limite_inferior
    while diminuendo_atual <= limite_superior:
        operacao_um_a_dez('S',diminuendo_atual)
        diminuendo_atual += 1

    show(50*'=')
    show(f'\nMULTIPLICAÇÃO')
    fator_atual = limite_inferior
    while fator_atual <= limite_superior:
        operacao_um_a_dez('M',fator_atual)
        fator_atual += 1

    show(50*'=')
    show(f'\nDIVISÃO')
    divisor_atual = limite_inferior
    while divisor_atual <= limite_superior:
        operacao_um_a_dez('D',divisor_atual)
        divisor_atual += 1
        
def operacao_um_a_dez(cod_operacao,numero):
    if cod_operacao == 'A':
        show(f'\nTabuada de adição de {numero}')
        a = 1
        while a <= 10:
            show(f'{numero} + {a} = {numero+a}')
            a += 1
    elif cod_operacao == 'S':
        show(f'\nTabuada de subtração de {numero}')
        s = 1
        while s <= 10:
            show(f'{numero+s} - {numero} = {s}')
            s += 1
    elif cod_operacao == 'M':
        show(f'\nTabuada de multiplicação de {numero}')
        m = 1
        while m <= 10:
            show(f'{numero} x {m} = {(numero * m)}')
            m += 1
    elif cod_operacao == 'D':
        show(f'\nTabuada de divisão de {numero}')
        d = 1
        while d <= 10:
            show(f'{numero*d} ÷ {numero} = {(numero*d/numero)}')
            d += 1
    else:
        show('Por favor, tenha certeza de digitar o código corretamente!')
        show('A - Adição')
        show('S - Subtração')
        show('M - Multiplicação')
        show('D - Divisão')

main()
