#38. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

#entrada
num1 = int(input('Qual o primeiro numerador? '))
den1 = int(input('Qual o primeiro denominador? '))
num2 = int(input('Qual o segundo numerador? '))
den2 = int(input('Qual o segundo número? '))

#proces
den = den1 * den2
num11 = den / den1 * num1
num22 = den / den2 * num2
numm = num11 + num22

#saída
print('Ao somar, encontra-se a fração',numm,'/',den)