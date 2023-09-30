#3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

#entrada
minutos = int(input('Insira um valor em minutos:'))

#process
hor = minutos // 60
min = minutos % 60

#saída
print('Isso corresponde a',hor,'horas e',min,'minutos')