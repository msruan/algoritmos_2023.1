#1/n - (n-1)/2 + 3/(n-2)... 1/n
# 1/3 - 2/2 + 3/1 
# 1/4 - 3/2 + 3/2 - 1/4  + 
from funcao import obter_inteiro_positivo, show
def main():
    numero = obter_inteiro_positivo('Manda um número: ')
    resultado = fracao(numero)
    float_to_fracao(resultado)
def fracao(n):
    if n == 2:
        show('Foi necessária uma operação!')
        return 0
    somador_fracoes = 1/n - (n-1)/2
    #- 0,666... se n = 3
    #1/4 - 3/2 = -1,25 se n = 4

    contador = 2
    numerador = 1
    while True:
        if not(eh_impar(contador)):
            numerador = contador + 1
            denominador = n - contador
            if denominador == 0 or numerador == 0:
                break
            somador_fracoes += numerador/ denominador 
            #-0,666666666 + 3, se n = 3
        else:
            numerador = n - contador
            denominador = contador + 1
            if denominador == 0 or numerador == 0:
                break
            somador_fracoes -= numerador / (contador + 1)
        contador += 1
    show(f'Foram necessárias {contador - 1} operações...')
    return somador_fracoes
def float_to_fracao(n):
    show(f'S = {n}')
    #numa futura implementação, pretendo transformar o decimal em fracao visual!

def eh_impar(num):
    if num % 2 == 1:
        return True
    return False
main()