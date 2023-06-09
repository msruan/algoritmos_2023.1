from funcao import obter_numero, show
def main():
    numero = obter_numero('Digite um número: ')
    show(f'Dividindo-o sucessivamente por 2, temos o resto {resto_por_dois(numero)}')
    pass
def resto_por_dois(numero):
    resto = 2
    while resto > 1:
        resto = numero % 2
        numero /= 2 
    return None
main()