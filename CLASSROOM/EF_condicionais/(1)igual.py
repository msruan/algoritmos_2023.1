def main() :
    um = float(input('Digite o primeiro número: '))
    dois = float(input('Digite o segundo número: '))
    tres = float(input('Digite o terceiro número: '))
    iguais = verify(um, dois, tres)
    saida(iguais)

def verify(um, dois, tres) :
    if um == dois and dois == tres:
        iguais = 3
    if (um == dois and dois != tres) or (um != dois and dois == tres) or (um == tres  and tres != dois):
        iguais = 2
    if um != dois and dois != tres and um != tres:
        iguais = 0
    return iguais

def saida(iguais) :
    print('Há',iguais,'números iguais!')    

main()