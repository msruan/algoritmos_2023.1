#2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

#entrada
horas = int(input('Quantas horas? '))
minutos = int(input('QUantos minutos?'))

#proces
rh = horas * 60
resposta = rh + minutos

#saída
print('Isso corresponde a',resposta,'minutos')