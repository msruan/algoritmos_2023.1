def main():
    a = obter_inteiro_positivo()
    print(a)
    print(type(a))
def insert(text):
    texto = input(text)
    while not texto:
        texto = input(text)
    return texto
def show(*label,sep='',end='\n'):
    print(*label,sep=sep,end=end)

#numéricos
def obter_inteiro_positivo(numero='Digite um inteiro positivo: '):
    num = number(numero)
    if type(num) == int and num > 0:  
        return num
    else:
        show("Erro! Digite um inteiro positivo!")
        return obter_inteiro_positivo()
    
def obter_inteiro_maior_que_um():
    show('Atenção, digite um inteiro maior que 1!\n')
    num = inteiro()
    if num <= 1:
        show("Erro! Número deve ser maior que 1!\n")  
        return obter_inteiro_maior_que_um()
    return num
def inteiro(num='Digite um inteiro: '):
    while not eh_numero(num):
        num = insert('Por favor, digite um inteiro: ')
    if eh_float(num):
        return inteiro()
    else:
        return int(num)

def number(num):
    while not eh_numero(num):
        num = insert('Por favor, digite um número: ')
    if eh_float(num):
        return float(num)
    else:
        return int(num)
    
def eh_digito(num):
    return (48 <= ord(num) <= 57)

def eh_numero(num):
    ha_nums = False
    ha_um_ponto = False
    primeiro = 0
    if eh_traco(num[0]):
        primeiro = 1

    for i in range(primeiro,len(num)):
        if eh_digito(num[i]):
            ha_nums = True
        elif eh_ponto(num[i]):
            if ha_um_ponto:
                return False
            ha_um_ponto = True
        else:
            return False
    return ha_nums
    
def eh_traco(num):
    return (ord(num) == 45)

def eh_ponto(num):
    return ord(num) == 46
def eh_float(num):
    for char in num:
        if char == '.':
            return True
    return False
