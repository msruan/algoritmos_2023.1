from funcao import show, obter_inteiro_maior_que_um
def main():
    limite_inferior = obter_inteiro_maior_que_um('Digite o limite inferior: ')
    limite_superior = obter_inteiro_maior_que_um('Digite o limite superior: ')
    if limite_superior <= limite_inferior:
        show("Por favor, tenha certeza de que o limite superior é maior que o inferior!")
        return main()
    obter_pares_no_limite(limite_inferior, limite_superior)
def obter_pares_no_limite(limite_inferior, limite_superior):
    show(f'Pares de {limite_inferior} a {limite_superior}:')
    for i in range(limite_inferior,limite_superior+1):
        if i % 2 == 0:
            show(f' {i};',end='')
main()