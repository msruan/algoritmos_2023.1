from my_array_utils import push
from my_strings_utils import split
from my_io_utils import show, obter_texto
from my_arraystring_utils import length, buscar
def main():
    vetor = split(obter_texto("Por favor, digite os elementos do vetor separados por ;\n>>>"),';')
    if ha_repetidos(vetor):
        show('Sim, há repetidos!')
    else:
        show('Não há repetidos!')

def ha_repetidos(vetor):
    verificados = []
    for i in range(length(vetor)):
        if buscar(verificados,vetor[i]):
            return True
        verificados = push(verificados,vetor[i]) 
    return False

main()