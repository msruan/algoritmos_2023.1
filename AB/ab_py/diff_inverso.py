#32. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

#entrada
num = int(input('Qual o número? '))

#process
cen = num // 100
dez = (num % 100) // 10
un = (num % 100) % 10
un_cen = un * 100
inverso = un_cen + dez * 10 + cen
diff = num - inverso

#saída
print('A diferença é',diff)