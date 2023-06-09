from funcao import show, obter_inteiro_maior_que_um
from funcao_math import eh_primo
def main():
    limite_inferior = obter_inteiro_maior_que_um('Digite o limite inferior: ')
    limite_superior = obter_inteiro_maior_que_um('Digite o limite superior: ')
    if limite_superior <= limite_inferior:
        show("Por favor, verifique suas entradas!")
        return main()
    obter_primos_no_limite(limite_inferior, limite_superior)
def obter_primos_no_limite(limite_inferior, limite_superior):
    show(f'Primos de {limite_inferior} a {limite_superior}:',end='')
    for i in range(limite_inferior,limite_superior+1):
        if eh_primo(i):
            show(f' {i};',end='')
main()