from funcao import obter_inteiro_positivo, eh_divisor, show
def main():
    quantos_nums = obter_inteiro_positivo('Quantos números você deseja? ')
    mostrar_divisores(quantos_nums)
def mostrar_divisores(quant):
    count = 0
    while count < quant:
        numero = obter_inteiro_positivo('Diga um número: ')
        show(f'Divisores de {numero}: ',end='')
        candidato = numero
        while candidato > 0:
            if eh_divisor(numero,candidato):
                show(f'{candidato} ',end='')
            candidato -= 1
        count += 1
main()