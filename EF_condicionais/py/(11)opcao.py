#11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores possíveis para a variável opção são 1, 2 e 3.

def main() :
    opcao = int(input('Qual a opção desejada? '))
    num1 = float(input('Qual o número um? '))
    num2 = float(input('Qual o segundo número? '))
    num3 = float(input('E o terceiro? '))
    num = verify(opcao,num1,num2,num3)
    saida(num)

def verify(opcao,num1,num2,num3):
    if opcao == 1:
        num = num1
    if opcao == 2:
        num = num2
    if opcao == 3:
        num = num3
    return num

def saida(num):
    print('O número escolhido foi',num,'!')
    
main()