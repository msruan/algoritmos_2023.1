#11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

#entrada
num = int(input('Insira o número de 3 dígitos:'))

#proces
cen_to_un = num // 100 #aqui é o número q era centena e vai ser unidade
dezena = (num % 100) // 10
un_to_cen = (num % 100) % 10
inverso = (un_to_cen * 100) + (dezena * 10) + cen_to_un

#saída
print('Esse número invertido fica',inverso)