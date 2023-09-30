from funcao import obter_inteiro_positivo,mmc,show
def main():
    a = obter_inteiro_positivo("Digite o primeiro número: ")
    b = obter_inteiro_positivo("Digite o segundo número: ")
    show(f'O mmc de {a} e {b} é {mmc(a,b)}.')
main()