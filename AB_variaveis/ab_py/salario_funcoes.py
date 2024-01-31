#entrada
def main() :
    salario = float(input('Insira o valor em reais:'))
    aumento = calculo(salario)
    saida(aumento)

#process
def calculo(salario) :
    por_cem = salario / 100
    aumento = salario + por_cem * 25
    return aumento

#saída
def saida(aumento) :
    print("Com o aumento, o salário passa a ser de",aumento,'reais')

main()