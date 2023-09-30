def main():
    lado1 = float(input('Digite o primeiro lado: '))
    lado2 = float(input('Digite o segundo lado: '))
    lado3 = float(input('Digite o terceiro lado: '))
    tipo = verify(lado1,lado2,lado3)
    saida(tipo)

def verify(lado1,lado2,lado3):
    if (lado1 + lado2 >= lado3 and lado2 + lado3 >= lado1 and lado1 + lado3 > lado2) and  (lado1 != 0 and lado2 != 0 and lado3 != 0):
        if lado1 == lado2 and lado2 == lado3:
            tipo = 'equilátero'
        elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3 :
            tipo = 'escaleno'
        else:
            tipo = 'isósceles'
    else:
       tipo = False
    return tipo

def saida(tipo):
    if tipo == False:
        print("Não formam um triângulo!")
    else:
        print("Formam um triângulo",tipo,'!')

main()