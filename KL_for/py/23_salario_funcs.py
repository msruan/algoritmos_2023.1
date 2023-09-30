'''Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
horas trabalhadas e o seu no de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
líquido do funcionário.'''
from funcao import show, obter_inteiro_positivo, insert

def main():
    quantidade_de_funcs = obter_inteiro_positivo('Quantos funcionários você quer catalogar? ')
    salario_funcs(quantidade_de_funcs)
    
    
def salario_funcs(quantidade):
    for i in range(quantidade):
        cod_do_func = obter_inteiro_positivo('Digite o código identificador do funcionário: ')
        nome_do_func = insert("Digite o nome do funcionário: ")
        horas_trabalhadas = obter_inteiro_positivo('Digite a quantidade de horas trabalhadas: ')
        num_de_dependentes = obter_inteiro_positivo('Digite o nº de dependentes: ')
        show(f'\nFuncionário: {nome_do_func} \nCódigo: {cod_do_func}\nHoras trabalhadas: {horas_trabalhadas}\n')
        salario_liquido = calcular_salario(horas_trabalhadas,num_de_dependentes)
        show(f'Salário: {salario_liquido}\n')     
        show('=' * 50,'\n')   
    

def calcular_salario(horas, dependentes):
    salario_bruto = 12 * horas + 40 * dependentes
    inss = 0.085 * salario_bruto
    ir = 0.05 * salario_bruto
    show(f'Descontos: \nINSS: R${inss}\nIR: R${ir}\n')
    return (salario_bruto - inss - ir)


main()