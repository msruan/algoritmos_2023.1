#8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

#entrada
prim = float(input('Digite o primeiro número'))
seg = float(input("insira o segundo número"))

#process
soma = prim + seg
sub = prim - seg
div = soma / sub

#saída
print('O resultado da divisão da soma entre os múmeros por sua diferença, equuivale a', div)