#IAC, é um método utilizado para medir a gordura corporal. Para o cálculo desse índice são utilizadas medidas antropométricas, como circunferência do quadril e altura.
#Dado o quadril (em cm) e a altura (em cm) de uma pessoa, calcule o IAC dessa pessoa.
#Fórmula do IAC: IAC = (quadril / (altura * sqrt(altura))) - 18
#Se o IAC estiver entre 0 e 8,9 a pessoa tá "Magra". Se o IAC estiver entre 9 e 20,9 tá "Normal". Se o IAC estiver entre 21 e 25,9, tá com "Sobrepeso", e por fim se o IAC estiver entre 26 e 29,9, está em "Obesidade grau 1". 
#Considerando a informação acima, além de mostrar o IAC da pessoa, calcule para ela qual o quadril mínino e máximo que ela deveria ter para ficar na faixa Normal.

import math
def main() :
    altura = float(input('Qual sua altura? (em centímetros) ')) / 100
    quadril = int(input('Qual a circunferência do seu quadril? (em centímetros) '))
    iac, qua_min, qua_max = calculo(altura, quadril)
    saida(iac, qua_min, qua_max)


def calculo(altura, quadril) :
    iac = (quadril / ((altura ** 0.5) * altura)) - 18
    qua_min = (9 + 18) * (altura * (altura ** 0.5))
    qua_max = (20.9 + 18) * (altura * (altura ** 0.5))
    return iac, qua_min, qua_max

def saida(iac, qua_min, qua_max) :
    print('O IAC é de',math.floor(iac),'. O quadril mínimo para se manter normal é de',math.floor(qua_min),', e o máximo é de',math.floor(qua_max))

main()