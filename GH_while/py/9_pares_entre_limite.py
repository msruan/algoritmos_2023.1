from funcao import show, obter_inteiro_maior_que_um
def main():
    limite_inferior = obter_inteiro_maior_que_um('Digite o limite inferior: ')
    limite_superior = obter_inteiro_maior_que_um('Digite o limite superior: ')
    if limite_superior <= limite_inferior:
        show("Por favor, tenha certeza de que o limite superior é maior que o inferior!")
        return main()
    obter_pares_no_limite(limite_inferior, limite_superior)
def obter_pares_no_limite(limite_inferior, limite_superior):
    atual = limite_inferior
    show(f'Pares de {limite_inferior} a {limite_superior}:',end='')
    while atual <= limite_superior:
        if not atual % 2:
            if (limite_superior - atual) == 1 or (limite_superior == atual):
                show(f' {atual}.',end='')
                return
            show(f' {atual},',end='')
        atual += 1
main()