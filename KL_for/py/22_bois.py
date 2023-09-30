from funcao import show, obter_inteiro_positivo, insert
from math import inf
def main():
    quantidade_de_bois = obter_inteiro_positivo('Quantos bois você quer catalogar? ')
    boiada(quantidade_de_bois)
    
def boiada(quantidade):
    maior_name = ''
    menor_name = ''
    maior_peso = -inf
    menor_peso = inf
    maior_cpf = -inf
    menor_cpf = inf
    for i in range(quantidade):
        cpf_do_boi = obter_inteiro_positivo('Digite o código identificador do boi: ')
        nome_do_boi = insert("Digite o nome do boi: ")
        peso_do_boi = obter_inteiro_positivo('Digite o peso do boi: ')
        if peso_do_boi >= maior_peso:
            maior_cpf = cpf_do_boi
            maior_name = nome_do_boi
            maior_peso = peso_do_boi
        if peso_do_boi <= maior_peso:
            menor_cpf = cpf_do_boi
            menor_name = nome_do_boi
            menor_peso = peso_do_boi
    show(f'\nMaior boi: \nCódigo: {maior_cpf}\nNome: {maior_name}\nPeso: {maior_peso}\n')
    show('=' * 50)
    show(f'\nMenor boi: \nCódigo: {menor_cpf}\nNome: {menor_name}\nPeso: {menor_peso}')

main()