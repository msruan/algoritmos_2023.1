from my_strings_utils import eh_numero
from my_arraystring_utils import length, revert, buscar

def delete(vetor,indice):
    lista = []
    for i in range(length(vetor)):
        if i != indice:
            lista = push(lista,vetor[i])
    return lista

def push(vetor,item):
    return vetor + [item]

def pop(vetor):
    x = []
    for i in range(length(vetor) - 1):
        x = push(x,vetor[i])
    return x

def bubble_sort(vetor_recebido,reverse=False):
    vetor = vetor_recebido[:]
    ha_trocas =False
    for i in range(length(vetor) - 1):
        ha_trocas = False
        for i in range(length(vetor) - 1):
            if vetor[i] > vetor[i+1]:
                atual = vetor[i] 
                proximo = vetor[i+1]
                vetor[i] = proximo
                vetor[i+1] = atual
                ha_trocas = True
        if not ha_trocas:
            break 
    if reverse:
        return revert(vetor)     
    return vetor 

def tirar_repetidos(vetor):
    verificados = []
    for i in range(length(vetor) -1):
        if not buscar(verificados,vetor[i]):
            verificados = push(verificados,vetor[i])
    return verificados

def reduce_produto(vetor):
    acumulado = 1
    for item in vetor:
        acumulado *= item
    return acumulado

def soma_vetor(vetor):
    soma = 0
    for item in vetor:
        if eh_numero(f'{item}'):
            soma += item
    return soma

def contar_ocorrencias_numero(lista, numero_buscado):
    ocorrencias = 0
    for item in lista:
        if item == numero_buscado:
            ocorrencias += 1
    return ocorrencias