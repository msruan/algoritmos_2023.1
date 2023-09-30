def main():
    ano = int(input('Em que ano você nasceu? '))
    mes = int(input('Em que mês você nasceu? '))
    dia = int(input('Em que dia você nasceu? '))
    ano2 = int(input('Em que ano estamos? '))
    mes2 = int(input('Em que mês estamos? '))
    dia2 = int(input('Em que dia estamos? '))
    meses, dias = calcular_idade(dia,dia2,mes,mes2,ano,ano2)
    saida(meses,dias)
def calcular_idade(dia,diatual,mes,mesatual,ano,anatual):
    meses = (anatual - ano) * 12
    dias = diatual - dia
    dios = dia - diatual
    if mes == mesatual:
        if dia==diatual:
            return meses, 0
        if dia < diatual:
            return meses, dias
        else:
            return meses - 1, 30 - dios
    if mes > mesatual:
        if dia==diatual:
            return meses - (mes - mesatual), 0
        if dia > diatual:
            return meses - 1 - (mes - mesatual), 30 - dios
        else:
            return meses - (mes - mesatual), dias
    else:
        if dia==diatual:
            return meses + (mesatual - mes), 0
        if dia < diatual:
            return meses, dias
        else:
            return meses - 1, 30 - dias
def saida(meses,dias):
    print(f"Corresponde a {meses} meses e {dias} dias! ")

main()