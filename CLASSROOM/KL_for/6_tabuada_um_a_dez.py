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
    for i in range(limite_inferior,limite_superior+1):
        operacao_um_a_dez('A',i)

    show(50*'=')
    show(f'\nSUBTRAÇÃO')
    for i in range(limite_inferior,limite_superior+1):
        operacao_um_a_dez('S',i)

    show(50*'=')
    show(f'\nMULTIPLICAÇÃO')
    for i in range(limite_inferior,limite_superior+1):
        operacao_um_a_dez('M',i)

    show(50*'=')
    show(f'\nDIVISÃO')
    for i in range(limite_inferior,limite_superior+1):
        operacao_um_a_dez('D',i)
        
def operacao_um_a_dez(cod_operacao,numero):
    if cod_operacao == 'A':
        show(f'\nTabuada de adição de {numero}')
        for i in range(1,11):
            show(f'{numero} + {i} = {numero+i}')
    elif cod_operacao == 'S':
        show(f'\nTabuada de subtração de {numero}')
        for i in range(1,11):
            show(f'{numero+i} - {numero} = {i}')
    elif cod_operacao == 'M':
        show(f'\nTabuada de multiplicação de {numero}')
        for i in range(1,11):
            show(f'{numero} x {i} = {(numero * i)}')
    elif cod_operacao == 'D':
        show(f'\nTabuada de divisão de {numero}')
        for i in range(1,11):
            show(f'{numero*i} ÷ {numero} = {(numero*i/numero)}')
    else:
        show('Por favor, tenha certeza de digitar o código corretamente!')
        show('A - Adição')
        show('S - Subtração')
        show('M - Multiplicação')
        show('D - Divisão')

main()
