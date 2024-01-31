#20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

#entrada
celsius = float(input('Insira uma temperatura em graus celsius:'))

#process
far = (celsius * 1.8) + 32

#saída
print('Em fahrenheit, essa temperatura é',far,'ºF')