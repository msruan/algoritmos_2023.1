from my_array_utils import revert
from my_strings_utils import split
from my_io_utils import show, obter_texto
def main():
    vetor = split(obter_texto("Por favor, digite os elementos do vetor separados por ;\n>>>"),';')
    show(revert(vetor))
main()