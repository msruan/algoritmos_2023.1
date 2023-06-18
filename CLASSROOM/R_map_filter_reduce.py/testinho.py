from my_utils import *
#12
def vetor_igual_ao_atual(vetor_atual,qualquer_ordem=False):
    vetor_pedido = obter_texto('Digite os números do vetor separados por vírgulas: \n>>>>')
    string_splitada = split(vetor_pedido,',')
    vetor_numerico = mapear(number,string_splitada)
    if qualquer_ordem:
        vetor_ordenado = bubble_sort(vetor_numerico)
        return (bubble_sort(vetor_atual) == vetor_ordenado)
    return vetor_atual == vetor_numerico