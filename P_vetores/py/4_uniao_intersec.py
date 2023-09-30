from my_array_utils import delete
from my_strings_utils import split
from my_io_utils import show, obter_texto
from my_arraystring_utils import length, buscar
from my_io_utils import obter_texto
def main():
    vetor_a = split(obter_texto("Por favor, digite os elementos do primeiro vetor separados por ;\n>>>"),';')
    vetor_b = split(obter_texto("Por favor, digite os elementos do segundo vetor separados por ;\n>>>"),';')
    vetor_c = vetor_a + vetor_b
    show(f'A união entre os vetores é {vetor_c}.')
    show(f'A intersecção é {intersec(vetor_a, vetor_b)}')

def intersec(vetor_recebido_a,vetor_recebido_b):
    vetor_a = vetor_recebido_a[:]
    vetor_b = vetor_recebido_b[:]
    interseccao = []
    for i in range(length(vetor_a)):
        if buscar(vetor_b,vetor_a[i]):
            index = buscar_index(vetor_b,vetor_a[i])
            interseccao = push(interseccao,vetor_b[index])
            vetor_b = delete(vetor_b,index)
    return interseccao

def push(vetor,item):
    return vetor + [item]
            

def buscar_index(lista,item): #in
    for i in range(length(lista)):
        if item == lista[i]:
            return i
    return False
main()