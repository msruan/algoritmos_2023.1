def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))
    num4 = int(input('Digite o quarto número: '))
    num5 = int(input('Digite o quinto número: '))
    #funções
    maior = verify_maior(num1,num2,num3,num4,num5)
    menor = verify_menor(num1,num2,num3,num4,num5)
    saida(maior,menor)

def verify_maior(num1, num2, num3, num4, num5):
    if num3 < num1 > num2 and num5 < num1 > num4:
        maior = num1
    if num3 < num2 > num1 and num5 < num2 > num4:
        maior = num2
    if num1 < num3 > num2 and num5 < num3 > num4:
        maior = num3
    if num3 < num4 > num2 and num5 < num4 > num1:
        maior = num4
    if num3 < num5 > num2 and num1 < num5 > num4:
        maior = num5
    return maior
def verify_menor(num1, num2, num3, num4, num5):
    if num3 > num1 < num2 and num5 > num1 < num4:
        menor = num1
    if num3 > num2 < num1 and num5 > num2 < num4:
        menor = num2
    if num1 > num3 < num2 and num5 > num3 < num4:
        menor = num3
    if num3 > num4 < num2 and num5 > num4 < num1:
        menor = num4
    if num3 > num5 < num2 and num1 > num5 < num4:
        menor = num5
    return menor

def saida(maior,menor):
    if maior == None:
        print('Por favor, digite 5 inteiros diferentes!')
    else:
        print(f"O maior número é {maior}!")
        print(f'O menor número é {menor}!')
        print("Fim do programa com êxito.")

main() 