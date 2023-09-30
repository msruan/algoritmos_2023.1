def main():
    ano = int(input('Em que ano você nasceu? '))
    mes = int(input('Em que mês você nasceu? '))
    dia = int(input('Em que dia você nasceu? '))
    ano2 = int(input('Em que ano estamos? '))
    mes2 = int(input('Em que mês estamos? '))
    dia2 = int(input('Em que dia estamos? '))
    if verificar_ano(ano,ano2) == False or verificar_mes(mes,mes2) == False or verificar_dia(dia,dia2) == False:
            print('Data inválida!') 
    else:
        anos = calcular_idade(dia,dia2,mes,mes2,ano,ano2)
        saida(anos)
            
def calcular_idade(dia,diatual,mes,mesatual,ano,anatual):
    anos = anatual - ano
    if mes == mesatual:
        if diatual >= dia:
            return anos
        else:
            return anos - 1
    if mesatual > mes:
        return anos
    else:
        return anos - 1
def verificar_ano(antiga,atual):
    return antiga > 0 and atual > 0 and atual >= antiga
def verificar_mes(antiga,atual):
    return 12 >= antiga > 0 and 12 >= atual > 0
def verificar_dia(antiga,atual):
    return 31 >= antiga > 0 and 31 >= atual > 0
def saida(anos):
    print(f"Você tem {anos} anos! ")

main()