#1/1 - 1/2 + 1/3... 1/n
from funcao import obter_inteiro_positivo, show
def main():
    numero = obter_inteiro_positivo('Manda um número: ')
    resultado = fracao(numero)
    float_to_fracao(resultado)
def fracao(n):
    if n == 2:
        return show("1/2")
    somador_fracoes = 1/2
    atual_denominador = 3
    contador = 3
    while atual_denominador <= n:
        if eh_impar(contador):
            somador_fracoes = somador_fracoes + 1 / atual_denominador
        else:
            somador_fracoes = somador_fracoes - 1 / atual_denominador
        atual_denominador += 1
        contador += 1
    show(f'Foram necessárias {contador - 2} operações...')
    return somador_fracoes
def float_to_fracao(n):
    show(n)
    #numa futura implementação, pretendo transformar o decimal em fracao visual!

def eh_impar(num):
    if num % 2 == 1:
        return True
    return False
main()