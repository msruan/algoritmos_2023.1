'''Joãozinho adora quebra-cabeças, essa é sua brincadeira favorita. O grande problema, porém, é que às vezes o jogo vem com uma peça faltando. Isso irrita bastante o pobre menino, que tem de descobrir qual peça está faltando e solicitar uma peça de reposição ao fabricante do jogo. Sabendo que o quebra-cabeças tem N peças, numeradas de 1 a N e que exatamente uma está faltando, ajude Joãozinho a saber qual peça ele tem de pedir.

Escreva um programa que, dado um inteiro N e N - 1 inteiros numerados de 1 a N, descubra qual inteiro está faltando.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A entrada contém 2 linhas. A primeira linha contém um inteiro N (2 ≤ N ≤ 1.000). A segunda linha contém N - 1 inteiros numerados de 1 a N (sem repetições).'''

def main():
    quantas_pecas = obter_inteiro_positivo()
    inserir_pecas = insert('Digite uma string com os quebra cabeças e iremos separá-la!')
    show(qual_peca_falta(quantas_pecas,inserir_pecas))
def qual_peca_falta(tamanho, as_pecas):
    pecas = partir(as_pecas)
    pecas = number_lista(pecas)
    peca_encontrada = False
    if len(pecas) != tamanho - 1:
        show("Tenha certeza de que enviou um número correto de peças!")
        novas_pecas = insert('Digite a lista de peças: ')
        return qual_peca_falta(tamanho, novas_pecas)
    quebra_cabeca = []
    for i in range(1,tamanho+1):
        quebra_cabeca.append(i)
    for item in quebra_cabeca:
        if item in quebra_cabeca:
            pass
        if item not in pecas and peca_encontrada == False:
            peca_encontrada = item
        else:
            show("Confira a entrada de dados novamente!")
            novas_pecas = insert('Digite a lista de peças: ')
            return qual_peca_falta(tamanho, novas_pecas) 
    return peca_encontrada
    


def juntar(string, separador=' '):
    new_string = ''
    for char in string:
         if char != separador:
            new_string += char
    return new_string
def partir(stringa, separador=' '):
    new_string = ''
    string = stringa + separador
    lista = []
    for char in string:
        if char != separador:
            new_string += char
        else:
            lista.append(new_string)
            new_string = ''
    return lista

def number_lista(lista_recebida):
    lista = lista_recebida[:]
    for i in range(len(lista)):
        if eh_numero(lista[i]):
            lista[i] = number(lista[i])
    return lista



def insert(text):
    texto = input(text)
    while not texto:
        texto = input(text)
    return texto
def show(*label,sep='',end='\n'):
    print(*label,sep=sep,end=end)

#numéricos
def obter_inteiro_positivo(numero='Digite um inteiro positivo: '):
    num = number(numero)
    if type(num) == int and num > 0:  
        return num
    else:
        show("Erro! Digite um inteiro positivo!")
        return obter_inteiro_positivo()
    
def obter_inteiro_maior_que_um():
    show('Atenção, digite um inteiro maior que 1!\n')
    num = inteiro()
    if num <= 1:
        show("Erro! Número deve ser maior que 1!\n")  
        return obter_inteiro_maior_que_um()
    return num
def inteiro(num='Digite um inteiro: '):
    while not eh_numero(num):
        num = insert('Por favor, digite um inteiro: ')
    if eh_float(num):
        return inteiro()
    else:
        return int(num)

def number(num):
    while not eh_numero(num):
        num = insert('Por favor, digite um número: ')
    if eh_float(num):
        return float(num)
    else:
        return int(num)
    
def eh_digito(num):
    return (48 <= ord(num) <= 57)

def eh_numero(num):
    ha_nums = False
    ha_um_ponto = False
    primeiro = 0
    if eh_traco(num[0]):
        primeiro = 1

    for i in range(primeiro,len(num)):
        if eh_digito(num[i]):
            ha_nums = True
        elif eh_ponto(num[i]):
            if ha_um_ponto:
                return False
            ha_um_ponto = True
        else:
            return False
    return ha_nums
    
def eh_traco(num):
    return (ord(num) == 45)

def eh_ponto(num):
    return ord(num) == 46
def eh_float(num):
    for char in num:
        if char == '.':
            return True
    return False
main()