from funcao import obter_inteiro_positivo,mdc,show
def main():
    a = obter_inteiro_positivo("Digite o primeiro número: ")
    b = obter_inteiro_positivo("Digite o segundo número: ")
    show(f'O mdc de {a} e {b} é {mdc(a,b)}.')
main()