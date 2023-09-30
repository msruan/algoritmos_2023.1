def main() :
    prim = float(input('Digite o primeiro número: '))
    dois = float(input('Digite o segundo número: '))
    maior, menor = verify(prim,dois)
    saida(maior,menor)

def verify(prim, dois) :
    if prim == dois:
        maior = 0
    if prim > dois:
        maior = 1
        menor = 2
    if prim < dois:
        maior = 2
        menor = 1
    return maior, menor

def saida(maior,menor) :
    if maior == 0:
        print('Os números são iguais!')
    else:
        print(f'O {maior}º número é o maior e o {menor}º número é o menor!')

main()    