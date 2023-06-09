def main() :
    um = int(input('Digite um número inteiro: '))
    dois = int(input("Digite o segundo número: "))
    tres = int(input('Diga o terceiro: '))
    quatro = int(input('Qual o quarto número? '))
    cinco = int(input("E o quinto? "))
    media = media_numeros(um,dois,tres,quatro,cinco)
    saida(um,dois,tres,quatro,cinco,media)

def media_numeros(um,dois,tres,quatro,cinco) :
    media = (um + dois + tres + quatro + cinco) / 5
    return media

def saida(um,dois,tres,quatro,cinco,media) :
    print('A média é',media)
    if um > media:
        print("O primeiro número é maior que a média!")
    if dois > media:
        print('O segundo número é maior que a média! ')
    if tres > media:
        print('O terceiro número é maior que a média!')
    if quatro > media:
        print('O quarto número é maior que a média!')
    if cinco > media:
        print('O quinto número é maior que a média.')

main()