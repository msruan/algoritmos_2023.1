#37. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

#entrada
num  = int(input('Digite a idade em dias:'))

#process
anos = num // 365
mes = (num % 365) // 30
dias = (num % 365) % 30

#saída
print('Isso corresponde a',anos,'anos,',mes,'meses e',dias,'dias!')