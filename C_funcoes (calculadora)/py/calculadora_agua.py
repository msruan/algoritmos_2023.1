#Crie um programa que receba o peso e a atividade física diária de uma pessoa e calcule a quantidade de água que ela deve beber por dia. A quantidade de água recomendada é de 35 ml por quilo de peso para pessoas com atividade física moderada, e 45 ml por quilo de peso para pessoas com atividade física intensa. O resultado do cálculo deve ser exibido na tela. 

#entrada
def main() :
    print('Digite 0, se seu nível de atividade física for moderado, ou digite 1 caso seja intenso.')
    ativ = int(input('Qual o seu nível de atividade física?(0 ou 1)'))
    peso = float(input('Quantos kgs você pesa? '))
    agua = calculo(ativ,peso)
    saida(agua)

def calculo(ativ,peso) :
    agua = (35 +(ativ * 15)) * peso
    return agua

def saida(agua) :
    print('A quantidade de água recomendada é',agua,'mls.')
    print('Lembre-se que uma boa hidratação é vital para o bom funcionamento do corpo!')

main()
