from funcao import show, obter_inteiro_positivo
def main():
    numero = obter_inteiro_positivo('Quer quantos números? ')
    sequencia_ate_n(numero)

def sequencia_ate_n(numero):
    sequencia = 0
    for i in range(1,numero+11):
        sequencia += i
        show(f'{sequencia}; ',end='')
main()