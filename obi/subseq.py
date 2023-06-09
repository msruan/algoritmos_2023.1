#mexer com indices
'''anotar os indices de cada um dos itens da lista em uma lista. so verificar se a ordem esta crescente
se indice menos um, falso, indice -1 '''
def main():
    a_and_b = separar(input())

    a = a_and_b[0]
    b = a_and_b[1]
    colecao = separar(input())
    a_verificar = separar(input())
    print(subseq(colecao,a_verificar))

def subseq(colecao, a_verificar):
    verificados = []
    for elemento in a_verificar:
        if elemento not in colecao:
            return 'N'
        for i in range(colecao):
            if elemento == colecao[i]:
                verificados.append(i)
    #verificados
    for i in range(verificados):
        if verificados[i] == len(verificados):
            return 'S'
        if verificados[i] > verificados [i+1]:
            return 'N'


        

def separar(string):
    stringa = string + ' '
    numero = ''
    lista = []
    for char in stringa:
        if char == ' ':
            lista.append(int(numero))
            numero = ''
        numero += char
    return lista
main()

main()