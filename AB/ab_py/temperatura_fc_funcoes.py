#21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

#entrada
def main() :
    far = float(input('Digite a temperatura em graus fahrenheit:'))
    celsius = calculo(far)
    saida(celsius)

#proces
def calculo(far) :
    celsius = (far - 32) * 1.8
    return celsius

#saída
def saida(celsius) :
    print('Essa temperatura em celsius corresponde a',celsius,'ºC')

main()