#28. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

#entrada
hours = int(input('Quantas horas? '))

#process
week = hours // 168
day = (hours % 168) // 24
hora = (hours % 168) % 24

#saída
print('Isso corresponde a',week,'semanas,',day,'dias e',hora,'horas!')