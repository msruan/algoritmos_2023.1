from my_arraystring_utils import buscar, mapear
from my_math_utils import inteiro

def split(string, separador=' '): #spllit
    item = ''
    string = string + separador
    lista = []
    for char in string:
        if char != separador:
            item += char
        else:
            lista.append(item)
            item = ''
    return lista

def join(string, separador=' '): #join
    new_string = ''
    for char in string:
         if char != separador:
            new_string += char
    return new_string

def char_para_maiusculo(char):
    if 97 <= ord(char) <= 122:
        return chr(ord(char) - 32)
    return char

def char_para_minusculo(char):
    if 65 <= ord(char) <= 90:
        return chr(ord(char) + 32)
    return char

def palavra_para_maiusculo(string):
    maiusculo = mapear(char_para_maiusculo,string)
    return maiusculo

def palavra_para_minusculo(string):
    minusculo = mapear(char_para_minusculo,string)
    return minusculo

def eh_ponto(num):
    return ord(num) == 46

def eh_letra(char):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,alfabeto)

def eh_minuscula(char):
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    return buscar(char,minusculas)

def eh_maiuscula(char):
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,maiusculas)

def contar_ocorrencias_caractere(texto, caractere_buscado, ignore_caixa_alta_e_baixa=True):
    ocorrencias = 0
    for char in texto:
        if char == char_para_maiusculo(caractere_buscado) or char == char_para_minusculo(caractere_buscado):
            ocorrencias += 1
    return ocorrencias

#number
def eh_numero(num):
    ha_nums = False
    ha_um_ponto = False
    primeiro = 0
    if eh_ponto(num[0]):
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

def eh_digito(num):
    for i in range(10):
        if num == str(i):
            return True
    return False

def eh_float(num):
    for char in num:
        if char == '.':
            return True
    return False

def float_int_para_int(real):
    inteirinho = ''
    for char in str(real):
        if not eh_ponto(char):
            inteirinho += char
            continue
        return inteiro(inteirinho)