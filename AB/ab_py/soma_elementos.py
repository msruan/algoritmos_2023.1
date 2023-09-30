#35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

#entrada
num = int(input("Digite o número de 4 dígitos: "))

#proces
m = num // 1000
c = (num % 1000) // 100
d = ((num % 1000) % 100) // 10
u = ((num % 1000) % 100) % 10
soma = m + c + d + u

#saída
print('A soma dos algarismos é',soma)