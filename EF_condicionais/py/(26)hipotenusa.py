def main():
    lado1 = float(input('Digite a medida do primeiro lado: '))
    lado2 = float(input('Digite a medida do segundo lado: '))
    lado3 = float(input('Digite a medida do terceiro lado: '))
    hipotenusa, c = verificar_hipotenusa(lado1,lado2,lado3)
    saida(hipotenusa, c)

def verificar_hipotenusa(l1,l2,l3):
    if l2 < l1 > l3:
        hipo = l1
        catetos = l2, l3
    if l3 < l2 > l1:
        hipo = l2
        catetos = l1,l3
    if l1 < l3 > l2:
        hipo = l3
        catetos = l1,l2
    return hipo, catetos
def saida(h,c):
    print(f'A  hipotenusa é ({h}) e os catetos são {c}!')

main()