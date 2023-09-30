#5. Leia 3 (três) números e escreva-os em ordem crescente.
def main() :
    um = float(input('Digite o primeiro número: '))
    dois = float(input("Insira o segundo número: "))
    tres = float(input('Forneça o terceiro: '))
    cres = verify(um,dois,tres)
    menor, meio, maior = calculo(um,dois,tres,cres)
    saida(cres,menor,meio,maior)
    
def verify(um, dois, tres) :
    if um == dois and dois == tres:
        cres = 0
    if um > dois and dois > tres:
        cres = 321
    if tres > dois and dois > um:
        cres = 123
    if dois > tres and tres > um:
        cres = 132
    if um > tres and tres > dois:
        cres = 231
    if tres > um and um > dois:
        cres = 213
    if dois > um and um > tres:
        cres = 312
    if um == dois and um < tres:
        cres = 1243
    if um == tres and um < dois:
        cres = 1342
    if dois == tres and um > tres:
        cres = 2341
    if um == dois and um > tres:
        cres = 3412
    if um == tres and um > dois:
        cres = 2413
    if dois == tres and um < tres:
        cres = 1423
    return cres

def calculo(um, dois, tres, cres) :
    if cres == 0:
        menor = False
        maior = False
        meio = False
    if cres != 0 and cres < 1000:
        menor = cres // 100
        if menor == 1:
            menor = um
        if menor == 2:
            menor = dois
        if menor == 3:
            menor = tres

        meio = cres % 100 // 10
        if meio == 1:
            meio = um
        if meio == 2:
            meio = dois
        if meio == 3:
            meio = tres

        maior = cres % 100 % 10
        if maior == 1:
            maior = um 
        if maior == 2:
            maior = dois
        if maior == 3:
            maior = tres
    if cres > 1000:
        if cres % 1000 // 100 == 4:
            menor = cres // 1000
            if menor == 1:
                menor = um
                maior = False
                meio = False
            if menor == 2:
                menor = dois
                maior = False
                meio = False
            if menor == 3:
                menor = tres
                maior = False
                meio = False
        elif cres % 1000 % 100 // 10 == 4:
            maior = cres // 1000
            if maior == 1:
                maior = um
                menor = False
                meio = False
            if maior == 2:
                maior = dois
                menor = False
                meio = False
            if maior == 3:
                maior = tres
                menor = False
                meio = False
    return menor, meio, maior


def saida(cres, menor, meio, maior) :
    if cres > 0 and cres < 1000:
        print('Em ordem crescente temos',menor,',',meio,'e',maior,'!')
    if cres == 0:
        print('Os números são iguais!')
    if cres % 1000 // 100 == 4:
        print('O número',menor,'é o menor, e os outros são iguais!')
    if cres % 1000 % 100 // 10 == 4:
        print('Dois números são iguais e o menor é o',maior,'!')
    
main()