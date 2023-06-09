#Leia N e escreva todos os números inteiros pares de 1 a N.
from funcao import show, obter_inteiro_maior_que_um, eh_par
def main():
    numero = obter_inteiro_maior_que_um('Digite um inteiro positivo: ')
    obter_pares_ate_n(numero)
def obter_pares_ate_n(num):
    show(f'Pares de 1 a {num}:',end='')
    for i in range(1,num+1):
        if eh_par(i):
            show(f' {i};',end='')
main()


