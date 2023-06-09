from funcao import obter_inteiro_maior_que_um, show
def main():
    numero = obter_inteiro_maior_que_um('Digite um inteiro positivo: ')
    show(f'Quadrado mais próximo: {obter_quadrados_ate_n(numero)}')
    
def obter_quadrados_ate_n(num):
    if num == 0 or num == 1 or num == 2:
        return 1
    expoente = 0
    for i in range(num):
        if i ** 2 > num:
            return expoente
        expoente = i ** 2
main()