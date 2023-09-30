#Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.
from funcao import show, obter_inteiro_positivo
def main():
    num_a_verificar = obter_inteiro_positivo('Digite o número que deseja verificar seus múltiplos: ')
    limite_inferior = obter_inteiro_positivo('Digite o limite inferior: ')
    limite_superior = obter_inteiro_positivo('Digite o limite superior: ')
    if limite_superior <= limite_inferior:
        show("Por favor, tenha certeza de que o limite superior é maior que o inferior!")
        return main()
    obter_multiplos_no_limite(limite_inferior, limite_superior,num_a_verificar)
def obter_multiplos_no_limite(limite_inferior, limite_superior,numero):
    atual = limite_inferior
    show(f'\nMúltiplos de {numero} no intervalo de {limite_inferior} a {limite_superior}:\n')
    while atual <= limite_superior:
        if not atual % numero:
            show(f'{atual}; ',end='')
        atual += 1
main()