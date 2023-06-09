def inputo(label):
    texto = input(label)
    while not texto:
        texto = input(label)
    return texto
def pinto(*label):
    print(*label)
    '''antiga number:
    numero = 0
    contador = 1
    ponto = None
    for i in range(len(num)):
        if eh_digito(num[i]):
            numero += (10 ** i) * int(num[i])
        if eh_ponto(num[i]):
            ponto = i
            break
    if ponto == None:
        if eh_traco == num[0]:
            numero *= -1
        return numero
    for a in range(ponto+1,len(num)):
        numero += (10 ** -contador) * int(num[a])
        contador += 1
    if eh_traco == num[0]:
        numero *= -1
    return numero
'''