#4. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

#entrada
cotação = float(input('Um dólar corresponde a quantos reais? '))
dolar = float(input('Insira um valor em dólar:'))

#process
real = dolar * cotação

#saída
print('Isso corresponde a',real,'reais')