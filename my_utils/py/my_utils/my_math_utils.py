from my_strings_utils import eh_numero,eh_float, float_int_para_int
from my_array_utils import bubble_sort, length
from random import randint
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


#eh ...?
def eh_inteiro(num):
    if (eh_numero(num)) and (not eh_float(num)):
        return True
    return False

def eh_tipo_inteiro(num):
    return(type(num) == int)

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

def eh_positivo(num):
    return (num > 0)

def eh_negativo(num):
    return (num < 0)

def eh_multiplo(candidato,numero):
    return (candidato % numero == 0)
        

def eh_numero_perfeito(num):
    lista_divisores = divisores(num) 
    del(lista_divisores[-1])
    sum = 0
    for item in lista_divisores:
        sum += item
    return (sum == num)

def fabrica_eh_multiplo(numero):
    def ehh_multiplo(candidato):
        return candidato % numero == 0
    return ehh_multiplo

#math básicas
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

def media(somatorio,quantidade):
    if somatorio != 0 and quantidade > 0:
        return somatorio / quantidade
    elif somatorio == 0 and quantidade > 0:
        return 0
    return None

def mediana(lista_recebida):
    lista = bubble_sort(lista_recebida)
    tamanho = length(lista)
    if tamanho == 0:
        return None
    elif eh_impar(tamanho):
        mediana = lista[float_int_para_int(((tamanho + 1) / 2) - 1)]#formula da mediana
    elif eh_par(tamanho):
        mediana = ((lista[float_int_para_int((tamanho/2)-1)] + lista[float_int_para_int((tamanho/2))]) / 2)
    return mediana

def fatorial(num):
    if num == 1 or num == 0:
        return 1
    return num * fatorial(num - 1)

def divisores(num):
    lista_divisores = []
    for i in range(1,num+1):
        if num % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def elevar_a_fator(num,fator=2):
    return num ** fator

def raiz_quadrada(num):
    return num ** (1/2)

def raiz_cubica(num):
    return num ** (1/3)

def raiz(num,indice):
    return num ** (1/indice)

def gerar_randomico(minimo,maximo):
    return randint(minimo,maximo)

