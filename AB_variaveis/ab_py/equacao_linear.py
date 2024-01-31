#Um sistema de equações lineares do tipo , pode ser resolvido segundo mostrado abaixo

#entrada
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
d = float(input('Digite o valor de d: '))
e = float(input('Digite o valor de e: '))
f = float(input('Digite o valor de f: '))

#proces
x = (c * e) - (b * f) / (a * e) - (b * d)
y = (a * f) - (c * d) / (a * e) - (b * d)

#saida
print('O valor de x é:',x)
print('O valor de y é:',y)
