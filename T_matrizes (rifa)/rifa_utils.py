#io
def show(label='',sep='',end='\n'): #print/mostrar_texto
    print(label,sep,end)

def mostrar_texto_inline(label='',sep=''): #print na mesma linha
    show(label,sep,end='')

def obter_texto(label='Digite um texto: '): #input/obter_texto
    texto = input(label)
    if texto == '':
        return obter_texto(label)
    return texto

def obter_resposta_sim_ou_nao(label='Sim ou Não?'):
    pergunta = obter_texto(f'{label} (S/N)\n>>>').upper()
    if pergunta == 'S' or pergunta == 'SIM':
        return True
    elif pergunta == 'N' or pergunta == 'NAO':
        return False
    else:
        return obter_resposta_sim_ou_nao(label)

#numéricos
def obter_numero(label='Digite um número:'):
    numero = obter_texto(label)
    if not eh_numero(numero):
        return obter_numero(label)
    return number(numero)

def obter_inteiro(label='Digite um inteiro:'):
    numero = obter_numero(label)
    if not eh_tipo_inteiro(numero):
        return obter_inteiro(label)
    return numero

def obter_numero_positivo(label='Digite um número positivo: '):
    num = input(label)
    if eh_numero(num):
        if number(num) > 0:
            return number(num)
    return obter_numero_positivo(label)

def obter_inteiro_positivo(label='Digite um inteiro positivo: '):
    numero = obter_numero(label)
    if not(eh_tipo_inteiro and numero > 0):
        return obter_inteiro_positivo(label)
    return numero
    

def obter_inteiro_minimo(tamanho_minimo,label=''):
    if label == '':#mensagem vazia?
        num = obter_inteiro(f'Por favor, digite um número maior ou igual a {tamanho_minimo}: ')
    else:
        num = obter_inteiro(label)
    if num < tamanho_minimo:
        return obter_inteiro_minimo(label)
    return num
    
def obter_inteiro_faixa(tamanho_minimo, tamanho_maximo,label='Insira um número: '):
    if label == '':#mensagem vazia?
        num = obter_inteiro(f'Por favor, insira um número de ho mínimo {tamanho_minimo} e de máximo {tamanho_maximo}: ')
    else:
        num = obter_inteiro(label)
    if tamanho_minimo > num or num > tamanho_maximo:
        return obter_inteiro_faixa(tamanho_minimo, tamanho_maximo, label)
    return num

#à parte
def limpar_tela():
    import os
    if os.name == 'posix':  # Para sistemas baseados em Unix (Linux, macOS, etc.)
        os.system('clear')
    elif os.name == 'nt':   # Para sistemas Windows
        os.system('cls')

def length(colecao):
    count = 0
    for _ in colecao:
        count += 1
    return count

#array_utils
def delete(vetor,indice):
    lista = []
    for i in range(length(vetor)):
        if i != indice:
            lista = push(lista,vetor[i])
    return lista

def push(vetor,item):
    return vetor + [item]

def eh_ponto(num):
    return ord(num) == 46



#number
def eh_numero(num):
    ha_nums = False
    ha_um_ponto = False
    primeiro = 0
    if eh_ponto(num[0]):
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

def eh_digito(num):
    for i in range(10):
        if num == str(i):
            return True
    return False

def eh_float(num):
    for char in num:
        if char == '.':
            return True
    return False

#math
def number(num):
    if eh_float(num):
        return float(num)
    elif eh_inteiro(num):
        return int(num)
    return num

def inteiro(num):
    if eh_inteiro(num):
        return int(num)
    return num

#eh ...?
def eh_inteiro(num):
    return eh_numero(num) and '.' not in str(num)

def eh_tipo_inteiro(num):
    return(type(num) == int)

def gerar_randomico(minimo,maximo):
    from random import randint
    return randint(minimo,maximo)

#happy utils
def interjeicao():
    interjeicoes = ["Uau!", "Incrível!", "Nossa!", "Caramba!", "Meu Deus!", "Passado!", "Impressionante!", "Que incrível!", "Uau, não acredito!", "Céus!", "Nossa senhora!", "Puxa vida!", "Não posso acreditar!", "Santo Deus!", "Caramba!", "Cara!", "Puxa!", "Nossa, isso é demais!", "Uau, que loucura!", "Jesus!"]
    return (interjeicoes[gerar_randomico(0,19)])

def bye():
    lista = ["Adeus, minha pimenta!", "Até mais, meu biscoitinho!", "Tchau, meu docinho de coco!", "Adeus, meu abacate!", "Até a próxima, meu brigadeiro!", "Tchau, meu pão de queijo!", "Adeus, meu bombonzinho!", "Até logo, minha pipoca!", "Tchauzinho, meu sorvetinho!", "Adeus, minha paçoquinha!", "Até mais, meu petit gateau!", "Tchau, meu cupcake!", "Adeus, meu marshmallow!", "Até a próxima, minha gelatina!", "Tchau, meu bolo de cenoura!", "Adeus, minha cocada!", "Até logo, minha torta de limão!", "Tchauzinho, meu suspiro!", "Adeus, meu chiclete!", "Até mais, meu pretzel!", "Tchau, meu nugget!", "Adeus, meu milkshake!", "Até a próxima, meu churros!", "Tchau, minha paçoca!", "Adeus, meu brigadeiro de panela!", "Até logo, minha geléia!", "Tchauzinho, meu crepe!", "Adeus, minha salada de frutas!", "Até mais, meu cheesecake!", "Tchau, meu biscoito da sorte!", "Adeus, meu sushi!", "Até a próxima, meu tempurá!", "Tchau, meu rolinho primavera!", "Adeus, meu macarrão!", "Até logo, meu bacon!", "Tchauzinho, meu frango a passarinho!", "Adeus, meu hambúrguer!", "Até mais, meu cachorro-quente!", "Tchau, minha pizza!", "Adeus, meu sorvete de casquinha!", "Até a próxima, meu milkshake!", "Tchau, meu bolo de chocolate!", "Adeus, meu croissant!", "Até logo, meu pão francês!", "Tchauzinho, meu waffle!", "Adeus, minha tapioca!", "Até mais, meu pão de mel!", "Tchau, meu brownie!", "Adeus, meu mousse!", "Até a próxima, minha geleia de mocotó!", "Tchau, meu macaron!", "Adeus, meu cuscuz!", "Até logo, meu panetone!", "Tchauzinho, meu brigadeiro branco!", "Adeus, minha coxinha!", "Até mais, meu pastel de feira!", "Tchau, minha empadinha!", "Adeus, meu esfiha!", "Até a próxima, meu churros!", "Tchau, meu pão de queijo!", "Adeus, minha tapioca!", "Até logo, minha geléia!", "Tchauzinho, meu brownie!", "Adeus, meu mousse!", "Até mais"]
    return show(lista[gerar_randomico(0,59)])