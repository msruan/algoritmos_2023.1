import math
def main():
    num = float(input("Digite um número: "))
    novo = arredondador(num)
    saida(novo)

def arredondador(num):
    if num - math.floor(num) < 0.5:
        return math.floor(num)
    else:
        return math.floor(num + 1)
def saida(num):
    print("Número arredondado:",num)
main()