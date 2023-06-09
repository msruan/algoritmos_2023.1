def main():
    print("Informe a data!")
    dia = int(input('Digite o dia da data: '))
    mes = int(input('Digite o mês da data: '))
    ano = int(input('Digite o ano da data: '))
    #funcoes
    data = verify(dia,mes,ano)
    saida(data)
    
def verify(dia,mes,ano):
    if (ano > 0) and (0 < mes <= 12):
        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
                if 29 >= dia > 0:
                    data = True
                else:
                    data = False
            else:
                if 28 >= dia > 0:
                    data = True
                else:
                    data = False
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or  mes == 10 or mes == 12:
            if 31 >= dia > 0:
                data = True
            else:
                data = False
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if 30 >= dia > 0:
                data = True
            else:
                data = False
    else:
        data = False
    return data
    
def saida(data):
    if data == False:
        print('Data inválida!')
    else:
        print("A data é válida!")

main()