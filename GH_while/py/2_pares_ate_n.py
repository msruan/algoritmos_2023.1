#Leia N e escreva todos os números inteiros pares de 1 a N.
from funcao import show, obter_inteiro_maior_que_um
def main():
    numero = obter_inteiro_maior_que_um('Digite um inteiro positivo: ')
    obter_pares_ate_n(numero)
def obter_pares_ate_n(num):
    if num == 2:
        return show('Pares até 1 a 2: 2.')
        
    atual = 1
    show(f'Pares de 1 a {num}:',end='')
    while atual < num:
        if not atual % 2:
            if (num - atual) == 1 or (num - atual == 2):
                show(f' {atual}.',end='')
                return
            show(f' {atual},',end='')
        atual += 1
main()


