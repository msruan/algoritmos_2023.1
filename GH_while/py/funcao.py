def insert(text):
    texto = input(text)
    while not texto:
        texto = input(text)
    return texto
def show(*label,sep='',end='\n'):
    print(*label,sep=sep,end=end)


#listas
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
def mapear(funcao,lista):
    lista_modificada = []
    for item in lista:
        lista_modificada.append(funcao(item))
    return lista_modificada

def buscar(item,lista):
    for elemento in lista:
        if item == elemento:
            return True
    return False
def filtrar(funcao_criterio,lista):
    filtrados = []
    for item in lista:
        if funcao_criterio(item):
            filtrados.append(item)
    return filtrados

def number_lista(lista_recebida):
    lista = lista_recebida[:]
    for i in range(len(lista)):
        if eh_numero(lista[i]):
            lista[i] = number(lista[i])
    return lista

def mmc(a,b):
    ememc = a
    while not(ememc % b == 0 and ememc % a == 0):
        ememc += 1
    return ememc

def mdc(a,b):
    emedc = a
    while not(a % emedc == 0 and b % emedc == 0):
        emedc -= 1
    return emedc

def mostrar_texto_inline(label):
    show(label,end='')

def mostrar_texto_caixa_alta(string):
    mapear(para_maiusculo,string)

def mostrar_texto_caixa_baixa(string):
    mapear(para_minusculo,string)


def para_maiusculo(char):
    if 97 <= ord(char) <= 122:
        return chr(ord(char) - 32)
    return char

def para_minusculo(char):
    if 65 <= ord(char) <= 90:
        return chr(ord(char) + 32)
    return char

def insert_tam_minimo(label,tamanho_minimo):
    while len(label) < tamanho_minimo:
        label = insert(f'Por favor, insira um texto de tamanho mínimo {tamanho_minimo}!')
    return label

def insert_tam_maximo(label,tamanho_maximo):
    while len(label) > tamanho_maximo:
        label = insert(f'Por favor, insira um texto de tamanho máx {tamanho_maximo}!')
    return label


def insert_tam_maximo(label,tamanho_minimo, tamanho_maximo):
    while tamanho_minimo > len(label) or len(label) > tamanho_maximo:
        label = insert(f'Por favor, insira um texto de tamanho mínimo {tamanho_minimo} e de tamanho máx {tamanho_maximo}!')
    return label

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
    
'''def eh_digito(num):
    return (48 <= ord(num) <= 57)'''
#v2
def eh_digito(num):
    for i in range(10):
        if num == str(i):
            return True
    return False

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

def obter_inteiro_negativo(label='Insira um inteiro negativo'):
    while num >= 0:
        num = num = number(label)
    return num
def obter_numero_minimo(tamanho_minimo,label='Insira um número: '):
    num = number(insert(label))
    while num < tamanho_minimo:
        num = number(insert(f'Por favor, digite um número maior ou igual a {tamanho_minimo}: '))
    return num
    
def obter_numero_minimo(tamanho_maximo,label='Insira um número: '):
    num = number(insert(label))
    while num > tamanho_maximo:
        num = number(insert(f'Por favor, digite um número menor ou igual a {tamanho_maximo}: '))
    return num
    
def obter_numero_faixa(tamanho_minimo, tamanho_maximo,num='Insira um número: '):
    while tamanho_minimo > len(num) or len(num) > tamanho_maximo:
        num = number(insert(f'Por favor, insira um número de ho mínimo {tamanho_minimo} e de máximo {tamanho_maximo}!'))
    return num
def eh_letra(char):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,alfabeto)

def eh_minuscula(char):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    return buscar

def eh_traco(char):
    return (char == '.')
#def eh_traco(num):
    #return (ord(num) == 45)

def eh_ponto(num):
    return ord(num) == 46
def eh_float(num):
    for char in num:
        if char == '.':
            return True
    return False
def eh_par(num):
    if num % 2 == 0:
        return True
    return False
def eh_impar(num):
    if num % 2 == 1:
        return True
    return False
def eh_primo(num):
    if num < 0:
        return False
    if num == 0 or num == 1 or num == 2 or num == 3 or num == 5 or num == 7:
        return True
    elif (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0):
        return False
    return True

def raiz_quadrada(num):
    return num ** 1/2

def raiz_cubica(num):
    return num ** 1/3

def raiz(num,indice):
    return num ** 1/indice

def contar_ocorrencias_caractere(texto, caractere_buscado, ignore_caixa_alta_e_baixa):
    ocorrencias = 0
    if ignore_caixa_alta_e_baixa:
        pass
    else:
        for char in texto:
            if char == caractere_buscado:
                ocorrencias += 1