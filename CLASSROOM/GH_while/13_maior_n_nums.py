from funcao import show, obter_inteiro_positivo
from math import inf
def main():
    quantidade_de_nums = obter_inteiro_positivo('Quantos números você quer calcular? ')
    o_maior = maior_n_nums(quantidade_de_nums)
    show(f'O maior desses números é {o_maior}')
    
def maior_n_nums(quantidade):
    contador = 1
    maior = -inf
    while contador <= quantidade:
        numero = obter_inteiro_positivo('Digite um inteiro positivo: ')
        contador += 1
        if numero > maior:
            maior = numero
    return maior

main()