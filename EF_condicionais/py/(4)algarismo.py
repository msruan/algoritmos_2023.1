def main() :
    num = int(input("Digite um número de dois dígitos!"))
    dezena, unidade = verify(num)
    saida(dezena,unidade)

def verify(num) :
    dezena = num // 10
    unidade = num % 10
    return dezena, unidade

def saida(dezena,unidade) :
    if dezena == unidade:
        print('Os dígitos são iguais!')
    else:
        print('Dígitos diferentes!')

main()
        