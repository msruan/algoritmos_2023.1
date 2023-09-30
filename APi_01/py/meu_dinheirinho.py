def main():
    nome = input('Qual o seu nome? ')
    print('Abaixo, digite 2 para Especialização, 3 para Mestrado ou 5 para Dutorado!')
    grau = int(input('Qual seu nível superior? ')) * 10
    hora_money = int(input('Quanto sua faculdade paga por aula base? '))
    aulas_sem = int(input('Quantas horas você trabalha por semana? '))
    exp = int(input('Há quantos meses você leciona? ')) // 12
    if exp % 12 > 6:
        exp += 1
    valor_aula_real = (hora_money + (hora_money * grau / 100) + (hora_money * (5 * exp) / 100))
    money_por_semana = aulas_sem * valor_aula_real
    salario_mensal = money_por_semana * 4.5
    #benefícios
    filhos = int(input('Quantos filhos menores de 6 anos voce têm? '))
    plano = float(input('Quanto você gasta com plano de saúde? '))

    #funçoes
    auxilio_creche, auxilio_plano, auxilio_comb = beneficios(filhos,plano,aulas_sem)
    inss, salario_sem_inss = desconto_inss(salario_mensal)
    ior = desconto_ior(salario_sem_inss)
    saida(nome,valor_aula_real,money_por_semana,salario_mensal,auxilio_creche,auxilio_plano,auxilio_comb,ior,inss)


def beneficios(filhos,plano,aulas_sem):
    if filhos != 0:
        auxilio_creche = 700 * filhos
    else:
        auxilio_creche = 0
    auxilio_comb = 3.25 * aulas_sem
    if plano != 0:
        if 0.5 * plano <= 500:
            auxilio_plano = 0.5 * plano
        else:
            auxilio_plano = 500
    return auxilio_creche, auxilio_plano, auxilio_comb
    
    #Descontos
    #*INSS
def desconto_inss(salario_mensal):
    if salario_mensal <= 1302:
        inss = 7.5 * salario_mensal / 100
    elif salario_mensal <= 2500:
        inss = 9 * salario_mensal / 100
    elif salario_mensal <= 3900:
        inss = 12 * salario_mensal / 100
    elif salario_mensal <= 7500:
        inss = 14 * salario_mensal / 100
    else:
        inss = 16 * salario_mensal / 100
    salario_sem_inss = salario_mensal - inss
    return inss, salario_sem_inss
    
    #*IOR
def desconto_ior(salario_sem_inss):
    if salario_sem_inss > 5000:
        ior = ((salario_sem_inss - 5000) * 27.5 / 100)
    else:
        ior = 0
    return ior
   
    #saída
def saida(nome,valor_aula_real,money_por_semana,salario_mensal,auxilio_creche,auxilio_plano,auxilio_comb,ior,inss):
    print('-'*10 + f' Olá {nome}! Aqui está seu contracheque detalhado. ' + '-'*10)
    print(f'Você ganha R$ {valor_aula_real} por aula. ')
    print(f'Por semana você ganha R$ {money_por_semana}.')
    print()
    print('-'*10 + ' Ganhos ' + '-'*10)
    print(f'Seu salário base mensal é de  R$ {salario_mensal}.')
    print(f'Auxílio creche: R$ {auxilio_creche}.')
    print(f'Ressarcimento do plano de saúde: R$ {auxilio_plano}.')
    print(f'Auxílio combustível: R$ {auxilio_comb}.')
    print(f'Salário bruto: R$ {salario_mensal + auxilio_comb + auxilio_plano + auxilio_creche}.')
    print()
    print('-'*10 + ' Descontos ' + '-'*10)
    print(f'Previdência: R$ {inss}.')
    print(f'Imposto de renda: R$ {ior}.')
    print(f'Total descontos: R$ {inss + ior}.')
    print()
    print('-'*10 + ' Salário líquido ' + '-'*10)
    print(f'R$ {salario_mensal + auxilio_comb + auxilio_plano + auxilio_creche - inss - ior}')
main()