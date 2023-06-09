from funcao import show, obter_inteiro_positivo
def main():
    quantidade_de_nums = obter_inteiro_positivo('Quantos números você quer calcular? ')
    sominha = soma_de_n_nums(quantidade_de_nums)
    a_media = media_de_n_nums(sominha, quantidade_de_nums)
    show(f'A soma dos números é igual a {sominha}, e sua média é igual a {a_media}!')

def soma_de_n_nums(quantidade):
    contador = 1
    somador = 0
    while contador <= quantidade:
        numero = obter_inteiro_positivo('Digite um inteiro positivo: ')
        contador += 1
        somador += numero
    return somador

def media_de_n_nums(soma, quantidade):
    return soma / quantidade
main()