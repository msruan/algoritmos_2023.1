from my_strings_utils import split
from my_io_utils import show, obter_texto
def main():
        vetor_a = split(obter_texto("Por favor, digite os elementos do primeiro vetor separados por ;\n>>>"),';')
        vetor_b = split(obter_texto("Por favor, digite os elementos do segundo vetor separados por ;\n>>>"),';')
        vetor_c = vetor_a + vetor_b
        show(vetor_c)
main()