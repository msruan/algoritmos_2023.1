1#8. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

def main() :
    print('Bem vindo à calculadora! Escolha uma opção abaixo.')
    print('1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão')
    opcao = int(input("Escolha uma opção: "))
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resposta = calculo(opcao,num1,num2)
    saida(resposta)

def calculo(opcao, num1, num2):
    if opcao == 1 :
        return (num1 + num2)
    if opcao == 2 :
        return (num1 - num2)
    if opcao == 3:
        return (num1 * num2)
    if opcao == 4:
        return (num1 / num2)

def saida(resposta):
    if resposta != None:
        print("A resposta é",resposta)
    else:
        print('Selecione uma operação válida!')

main()