#Leia N e escreva todos os números inteiros de 1 a N.
from funcao import show, obter_inteiro_maior_que_um
def main():
    numero = obter_inteiro_maior_que_um('Digite um inteiro positivo: ')
    obter_numeros_ate_n(numero)
def obter_numeros_ate_n(num):
    if num == 1:
        show('Só há o número 1!')
        return
    show(f'Inteiros de 1 a {num}:',end='')
    for i in range(1,num+1):
        show(f' {i};',end='')
main()


