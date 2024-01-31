#36. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

#entrada
def main() :
    anos = int(input('Quantos anos? '))
    mes = int(input('Quantos meses? '))
    dias = int(input('Quantos dias? '))
    idade = calculo(anos, mes, dias)
    saida(idade)

#process
def calculo(anos, mes, dias) :
    idade = anos * 365 + mes * 30 + dias 
    return idade

#saída
def saida(idade) :
    print("A idade é de",idade,'dias!')

main()