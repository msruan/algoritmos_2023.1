import math
def main() :
    peso = float(input("Qual o seu peso? "))
    porcento = float(input('Qual a porcentagem do seu peso que você deseja perder? '))
    semanas = float(input('Eqm quantas semanas pretende perder esse peso? '))
    intensidade = float(input('Qual a intensidade dos exercícios que você pratica?'))
    consumo_diario = float(input('Quantas kcal você vai consumir? '))
    gasto = calculo(peso, porcento, semanas, consumo_diario)
    saida(gasto)

def calculo(peso, porcento, semanas, consumo_diario) :
    cal_a_perder = peso * (porcento / 100) * 7700
    diario = cal_a_perder / (semanas * 7)
    gasto = consumo_diario + diario
    return gasto

def saida(gasto) :
    print('Você deverá gastar',math.floor(gasto),'kcals com suas atividades diárias.')
    print('Ou seja, considerando que normalmente você gasta 2000 kcals diariamente apenas existindo,\nvocê deverá gastar',math.floor((gasto - 2000)),'kcals em exercícios físicos.')

main()