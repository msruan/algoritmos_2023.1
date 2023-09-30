#5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

#entrada
num = int(input('Insira um número de 3 algarismos:'))

#process
cent = (num // 100) 
dez = (num % 100) // 10
uni = (num % 100) % 10
soma = cent + dez + uni

#saída
print("A soma dos algarismos desse número é",soma)