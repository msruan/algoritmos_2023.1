def main():
    a_and_b = separar(input())
    a = a_and_b[0]
    b = a_and_b[1]
    meu_estoque = estoque(a,b)
    pergunta = int(input())
    atual = pergunta
    while atual > 0:
        a_and_b = separar(input())
        tipo = a_and_b[0]
        tamanho = a_and_b[1]
        meu_estoque = vender(meu_estoque,tipo+1,tamanho+1)
        atual -= 1



def estoque(a,b):
    estoquinho = []
    for i in range(a):#tamanho
        em_estoque = separar(input())
        listinha = []
        for i in range(b):#pecas
            listinha.append(em_estoque[i])
        estoquinho.append(listinha)
    return estoquinho
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
def vender(estoque,tipo,tamanho):
    if estoque[tipo][tamanho] > 0:
        estoque[tipo][tamanho] -= 1
    return estoque
main()
