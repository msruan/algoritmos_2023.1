#9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).

#entrada
def main() :
    a = float(input('Digite o primeiro número:'))
    b = float(input('Insira o segundo número:'))
    saida(a,b)

#saída
def saida(a,b) :
    print('Invertendo, o primeiro número passa a ser',b,', e o segundo número vira',a)

main()