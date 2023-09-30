#7. Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

#entrada
prim = float(input('Insira o primeiro número:'))
seg  = float(input('Digite o segundo número:'))
terc = float(input('Informe o terceiro número:'))

#proces
soma = prim + seg
sub = seg - terc

#saída
print('A soma dos dois primeiros números é',soma)
print('A diferença entre os dois últimos é',sub)