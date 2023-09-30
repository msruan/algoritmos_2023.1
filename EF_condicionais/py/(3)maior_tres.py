def main() :
    prim = float(input("Digite o primeiro número: "))
    seg = float(input('Digite o segundo número: '))
    ter = float(input("DIgite o terceiro número: "))
    maior = verify(prim, seg, ter)
    saida(maior)

def verify(prim, seg, ter) :
    if prim == seg and  seg == ter:
        maior = 0
    if prim > seg and prim > ter:
        maior = 1
    if prim < seg and seg > ter:
        maior = 2
    if prim < ter and seg < ter:
        maior = 3
    if prim == seg and prim > ter:
        maior = 12
    if prim == ter and prim > seg:
        maior = 13
    if seg == ter and prim < seg:
        maior = 23
    return maior

def saida(maior) :
    if maior == 0:
        print('Todos os números são iguais!')
    if maior > 0 and maior <= 3:
        print('O ',maior,'º número é o maior!',sep="")
    if maior > 3:
        print('O ',maior // 10,'º e o ',maior % 10,'º número são os maiores!',sep="")

main()
    