#26. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

#entrada
dias = int(input('Quantos dias? '))

#process
semanas = dias // 7
days = dias % 7

#saída
print('Isso corresponde a',semanas,'semanas e',days,'dias!')