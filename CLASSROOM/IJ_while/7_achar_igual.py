from funcao import obter_numero, show
def main():
    num = obter_numero("Digite um número: ")
    lista(num)
    
def lista(primeiro_num):
    numero = None
    while numero != primeiro_num:
        numero = obter_numero("Digite outro número: ")
    return show('Número encontrado!')
main()