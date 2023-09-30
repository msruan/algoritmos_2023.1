#29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

#entrada
meses = int(input('Quantos meses? '))

#proces
anos = meses // 24
mes = meses % 24

#saída
print("Isso corresponde a",anos,'anos e',mes,'meses!')