#Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.
from funcao import show, obter_inteiro_maior_que_um
def main():
    numero = obter_inteiro_maior_que_um('Qual número será o limite superior? ')
    sominha = soma_de_um_ate_n(numero)
    show(f'A soma dos números é igual a {sominha}!')

def soma_de_um_ate_n(numero):
    contador = 0
    somador = 0
    while contador <= numero:
        somador += contador
        contador += 1 
    return somador
main()