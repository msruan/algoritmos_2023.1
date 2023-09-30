def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    operacao = operacoes(num1,num2)
    saida(operacao)

def operacoes(num1, num2):
    resto = num1 % num2
    if resto == 1:
        return f'Soma dos valores mais o resto: {num1+num2+1}'
    if resto == 2:
        if num1 % 2 == 0:
            if num2 % 2 == 0:
                return 'Ambos são pares!'
            else:
                return f'{num1} é par e {num2} é ímpar!'
        elif num2 % 2 == 0:
            return f'{num1} é ímpar e {num2} é par!'
        else:
            return 'Ambos são ímpares!'
    if resto == 3:
        return f'A soma dos números multiplicada por {num1} é igual a {(num1+num2)*num1}!'
    if resto == 4:
        if num2 != 0:
            return f'O resultado da soma dos números divida por {num2} é igual a {(num1+num2)/num2}!'
        else:
            return 'O segundo número é igual a 0!'
    else:
        return f'O quadrado de {num1} é {num1**2} e o quadrado de {num2} é {num2**2}!'

def saida(op):
    print(op)

main()