from funcao import obter_inteiro_maior_que_um, show
def main():
    numero = obter_inteiro_maior_que_um('Digite um inteiro positivo: ')
    show(f'Quadrado mais próximo: {obter_quadrados_ate_n(numero)}')
def obter_quadrados_ate_n(num):
    atual = 1
    expo = 1
    while expo < num:
        expo = atual ** 2
        ultimo_expo = (atual-1) ** 2
        if expo == num:
            return atual
        if expo > num :
           if num - ultimo_expo < expo - num:
              return ultimo_expo
           else:
              return expo
        atual += 1
main()