def main():
    lado1 = float(input('Digite o primeiro ângulo: '))
    lado2 = float(input('Digite o segundo ângulo: '))
    lado3 = float(input('Digite o terceiro ângulo: '))
    tipo = verify(lado1,lado2,lado3)
    saida(tipo)

def verify(lado1,lado2,lado3):
    if lado1 + lado2 + lado3 == 180 and (lado1 != 0 and lado2 != 0 and lado3 != 0):
        if lado1 == 90 or lado2 == 90 or lado3 == 90:
            tipo = 'retângulo'
        if lado1 < 90 and lado2 < 90 and lado3 < 90:
            tipo = 'acutângulo'
        elif lado1 > 90 or lado2 > 90 or lado3 > 90:
            tipo = 'obtusângulo'

    else:
       tipo = False
    return tipo

def saida(tipo):
    if tipo == False:
        print("Não formam um triângulo!")
    else:
        print("Formam um triângulo",tipo,'!')

main()