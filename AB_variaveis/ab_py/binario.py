#31. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

#entrada
num = int(input('Digite o binário:'))

#process
m = (num // 1000) * 8
c = ((num % 1000) // 100) * 4
d = (((num % 1000) % 100) // 10) * 2
u = (((num % 1000) % 100) % 10) 
dec = m + c + d + u

#saída
print('Esse número em decimal é:',dec)