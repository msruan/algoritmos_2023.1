'''Bem vindo às nossas utils! Segue o índice:
1 - INPUT/OUTPUT
1.1 - INPUTS NUMERICOS
2 - MATEMATICA
3 - STRINGS
4 - LISTA
'''
#1.INPUT/OUTPUT
def show(label='',sep='',end='\n'): #print/mostrar_texto
    print(label,sep,end)

def mostrar_divisao(*label,sep='',end='\n'): #print/mostrar_texto
    print(*label,sep,end)

def mostrar_texto_inline(label='',sep=''): #print na mesma linha
    show(label,sep,end='')

def mostrar_texto_caixa_alta(string=''): 
    show(mapear(para_maiusculo,string))

def mostrar_texto_caixa_baixa(string=''):
    mapear(para_minusculo,string)

def insert(label='Digite um texto: '): #input/obter_texto
    texto = input(label)
    if texto == '':
        return insert(label)
    return texto

def obter_texto_tam_minimo(tamanho_minimo,label=''):#label = aquela mensagemzinha que a gente manda pro input
    if label == '':#a mensagem está vazia?
        texto = insert(f'Por favor, insira um texto de tamanho mínimo {tamanho_minimo}!')
    else:
        texto = insert(label)
    if len(label) < tamanho_minimo:#tá no tamanho adequado?
        return obter_texto_tam_minimo()
    return texto

def obter_texto_tam_maximo(label,tamanho_maximo):
    if label == '':#a mensagem está vazia?
        texto = insert(f'Por favor, insira um texto de tamanho mínimo {tamanho_maximo}!')
    else:
        texto = insert(label)
    if len(label) > tamanho_maximo:#tá no tamanho adequado?
        return obter_texto_tam_maximo()
    return texto

def obter_texto_tam_min_maximo(label,tamanho_minimo, tamanho_maximo):
    if label == '':#a mensagem está vazia?
        texto = insert(f'Por favor, insira um texto de tamanho mínimo {tamanho_minimo} e de tamanho máx {tamanho_maximo}!!')
    else:
        texto = insert(label)
    if tamanho_minimo > len(label) or len(label) > tamanho_maximo:
        return obter_texto_tam_min_maximo()
    return texto

def obter_opcoes(label, opcoes):
    pass
"""==============================================================================================="""



#1.1 INPUTS NUMÉRICOS
def obter_numero(label='Digite um número:'):
    numero = insert(label)
    if not eh_numero(numero):
        return obter_numero(label)
    return number(numero)

def obter_inteiro(label='Digite um inteiro:'):
    numero = obter_numero(label)
    if not eh_tipo_inteiro(numero):
        return obter_inteiro(label)
    return numero

def obter_inteiro_positivo(label='Digite um inteiro positivo: '):
    numero = obter_numero(label)
    if not(eh_tipo_inteiro and numero > 0):
        return obter_inteiro_positivo(label)
    return numero
    
def obter_inteiro_negativo(label='Insira um inteiro negativo'):
    numero = obter_numero(label)
    if not(eh_tipo_inteiro(numero) and numero < 0):
        return obter_inteiro_positivo(label)
    return numero

def obter_numero_minimo(tamanho_minimo,label=''):
    if label == '':#mensagem vazia?
        num = obter_numero(f'Por favor, digite um número maior ou igual a {tamanho_minimo}: ')
    else:
        num = obter_numero(label)
    if num < tamanho_minimo:
        return obter_numero_minimo(label)
    return num
    
def obter_numero_maximo(tamanho_maximo,label='Insira um número: '):
    if label == '':#mensagem vazia?
        num = obter_numero(f'Por favor, digite um número menor ou igual a {tamanho_maximo}: ')
    else:
        num = obter_numero(label)
    if num > tamanho_maximo:
        return obter_numero_maximo(label)
    return num
    
def obter_numero_faixa(tamanho_minimo, tamanho_maximo,label='Insira um número: '):
    if label == '':#mensagem vazia?
        num = obter_numero(f'Por favor, insira um número de ho mínimo {tamanho_minimo} e de máximo {tamanho_maximo}: ')
    else:
        num = obter_numero(label)
    if tamanho_minimo > num or num > tamanho_maximo:
        return obter_numero_maximo(label)
    return num
"""==============================================================================================="""



#2.MATEMATICA
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

def number(num):
    if eh_float(num):
        return float(num)
    elif eh_inteiro(num):
        return int(num)
    return num


def inteiro(num):
    if eh_inteiro(num):
        return int(num)
    return num

def eh_inteiro(num):
    if (eh_numero(num)) and (not eh_float(num)):
        return True
    return False

def eh_tipo_inteiro(num):
    return(type(num) == int)
        
def divisores(num):
    lista_divisores = []
    for i in range(1,num+1):
        if num % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def eh_divisor(numero,candidato_a_divisor):
    return (numero % candidato_a_divisor == 0)

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

def eh_numero_perfeito(num):
    lista_divisores = divisores(num) 
    del(lista_divisores[-1])
    sum = 0
    for item in lista_divisores:
        sum += item
    return (sum == num)

def fatorial(num):
    if num == 1 or num == 0:
        return 1
    return num * fatorial(num - 1)

def raiz_quadrada(num):
    return num ** (1/2)

def raiz_cubica(num):
    return num ** (1/3)

def raiz(num,indice):
    return num ** (1/indice)
"""==============================================================================================="""

#3. STRINGS
def juntar(string, separador=' '): #join
    new_string = ''
    for char in string:
         if char != separador:
            new_string += char
    return new_string

def quebrar(stringa, separador=' '): #spllit
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

def quebrar_palavra(string): #spllit
    lista = []
    for char in string:
        lista.append(char)
    return lista

def mapear(funcao,colecao): #map
    if type(colecao) == list:
        lista_modificada = []
        for item in colecao:
            lista_modificada.append(funcao(item))
        return lista_modificada
    elif type(colecao) == str:
        string_modificada = ''
        for char in colecao:
            string_modificada += funcao(char)
        return string_modificada
    '''elif type(colecao) == tuple:
        lista_modificada = []
        for item in colecao:
            lista_modificada.append(funcao(item))
        return tuple(lista_modificada)'''        
    return colecao


def buscar(item,lista): #in
    for elemento in lista:
        if item == elemento:
            return True
    return False

def filtrar(funcao_criterio,lista): #filter
    filtrados = []
    for item in lista:
        if funcao_criterio(item):
            filtrados.append(item)
    return filtrados

def para_maiusculo(char):
    if 97 <= ord(char) <= 122:
        return chr(ord(char) - 32)
    return char

def para_minusculo(char):
    if 65 <= ord(char) <= 90:
        return chr(ord(char) + 32)
    return char

def eh_letra(char):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,alfabeto)

def eh_minuscula(char):
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    return buscar(char,minusculas)

def eh_maiuscula(char):
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,maiusculas)

def eh_traco(char):
    return (char == '-')
#def eh_traco(num):
    #return (ord(num) == 45)

def eh_ponto(num):
    return ord(num) == 46
def eh_float(num):
    for char in num:
        if char == '.':
            return True
    return False

def contar_ocorrencias_caractere(texto, caractere_buscado, ignore_caixa_alta_e_baixa):
    ocorrencias = 0
    for char in texto:
        if char == para_maiusculo(caractere_buscado) or char == para_minusculo(caractere_buscado):
            ocorrencias += 1
    return ocorrencias
def buscar_substring(string,substring):
    tamanho = len(substring)
    for i in range(len(string)):
        pass