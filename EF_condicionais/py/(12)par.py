def main():
    num = int(input('Digite um número inteiro: '))
    resposta = verify(num)
    saida(resposta)

def verify(num):
    if num % 2 == 0:
        resposta = "par"
    else:
        resposta = "ímpar"
    return resposta

def saida(resposta):
    print("O número é",resposta,'!')

main()