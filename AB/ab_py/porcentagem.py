#13. Leia um valor em real (R$), calcule e escreva 70% deste valor.

#entrada
real = float(input('Insira o valor do salário:'))

#proces
por_cem = real / 100
resposta = por_cem * 70

#saída
print('70% desse sálario é torna',resposta,'reais')