def main() :
    horas1 = float(input('Quantas horas o primeiro professor trabalhou? '))
    dinheiro1 = float(input('Quanto o primeiro professor ganhou por hora? '))
    horas2 = float(input('Quantas horas o segundo professor trabalhou? '))
    dinheiro2 = float(input('E quanto ele ganhou por hora? '))
    maior = calculo(horas1, dinheiro1, horas2, dinheiro2)
    saida(maior)
def calculo(horas1,dinheiro1,horas2,dinheiro2) :
    salario1 = horas1 * dinheiro1
    salario2 = horas2 * dinheiro2
    if salario1 > salario2 :
        maior = 1
    if salario1 < salario2 :
        maior = 2
    if salario1 == salario2:
        maior = 0 
    return maior
def saida(maior) :
    if maior == 0:
        print('Os salários são iguais!')
    if maior == 1:
        print("O primeiro professor ganhou mais!")
    if maior == 2:
        print('O segundo professor ganhou mais!')
main()