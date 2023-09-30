from funcao import show, obter_inteiro_positivo
def main():
    numero = obter_inteiro_positivo('Quer quantos números? ')
    sequencia_ate_n(numero)

def sequencia_ate_n(numero):
    sequencia = 0
    somador = 1
    while somador <= numero:
        sequencia += somador
        somador += 1 
        show(f'{sequencia}; ',end='')
main()