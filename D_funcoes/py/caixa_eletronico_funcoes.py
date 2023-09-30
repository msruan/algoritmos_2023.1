#Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o saque. Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.

#entrada
def main():
    din = int(input('Qual a quantia em dinheiro? '))
    cinquenta, vinte, dez, cinco, dois, um = calculo(din)
    saida(cinquenta, vinte, dez, cinco, dois, um)

#proces
def calculo(din):
    cinquenta = din // 50
    vinte = (din - (cinquenta * 50)) // 20
    dez = ((din - (cinquenta * 50)) - (vinte * 20)) // 10
    cinco = ((din - (cinquenta * 50)) - (vinte * 20) - (dez * 10)) // 5
    dois = ((din - (cinquenta * 50)) - (vinte * 20) - (dez * 10) - (cinco * 5)) // 2
    um = ((din - cinquenta * 50) - (vinte * 20) - (dez * 10) - (cinco * 5) - (dois * 2)) 
    return cinquenta, vinte, dez, cinco, dois, um 
       
#saída
def saida(cinquenta, vinte, dez, cinco, dois, um) :
    print('Cinquenta:',cinquenta,'notas, vinte:',vinte,'notas, dez:',dez,'notas, cinco:',cinco,'notas, dois:',dois,'notas, um:',um),'moedas.'

main()