'''A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.'''
from funcao import show, obter_inteiro_positivo, insert

def main():
    quantidade_de_habs = obter_inteiro_positivo('Quantos habitantes você quer catalogar? ')
    pesquisa(quantidade_de_habs)
    
    
def pesquisa(quantidade):
    habitantes = 0
    contador_filhos = 0
    soma_salarios = 0
    contador_salario_min = 0
    while habitantes < quantidade:
        num_de_filhos = obter_inteiro_positivo('Digite seu número de filhos: ')
        salario = obter_inteiro_positivo('Digite seu salário: ')
        
        if salario <= 1000:
            contador_salario_min += 1
        soma_salarios += salario  
        contador_filhos += num_de_filhos
        habitantes += 1
    show('')     
    show('=' * 50,'\n') 
    show(f'\nA média de salário é {soma_salarios / habitantes}')
    show(f'A média de número de filhos é {contador_filhos / habitantes}')
    show(f'O percentual de pessoas que ganham até 1000 reais é de {percentual(contador_salario_min, habitantes)}%\n')
    show('=' * 50,'\n') 
def percentual(num_a,num_b):
    return num_a / num_b * 100
    

def calcular_salario(horas, dependentes):
    salario_bruto = 12 * horas + 40 * dependentes
    inss = 0.085 * salario_bruto
    ir = 0.05 * salario_bruto
    show(f'Descontos: \nINSS: R${inss}\nIR: R${ir}\n')
    return (salario_bruto - inss - ir)


main()