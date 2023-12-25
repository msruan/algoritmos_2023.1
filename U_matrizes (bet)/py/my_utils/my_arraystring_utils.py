from my_array_utils import push
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
    elif type(colecao) == tuple:
        lista_modificada = []
        for item in colecao:
            lista_modificada.append(funcao(item))
        return tuple(lista_modificada)
    
def filtrar(funcao_criterio,lista): #filter
    filtrados = []
    for item in lista:
        if funcao_criterio(item):
            filtrados = push(filtrados,item)
    return filtrados
    
def length(colecao):
    count = 0
    for _ in colecao:
        count += 1
    return count

def revert(lista_recebida):
    lista_modificada = lista_recebida[:]
    for i in range(length(lista_recebida)):
        lista_modificada[i] = lista_recebida[-(i+1)] 
    return lista_modificada

def buscar(lista,item): #in
    for elemento in lista:
        if item == elemento:
            return True
    return False