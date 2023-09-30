from random import randint
import os
'''Bem vindo às nossas utils!'''

#1.INPUT/OUTPUT
def show(label='',sep='',end='\n'): #print/mostrar_texto
    print(label,sep,end)

def obter_texto(label='Digite um texto: '): #input/obter_texto
    texto = input(label)
    if texto == '':
        return obter_texto(label)
    return texto

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

"""==============================================================================================="""


#2.MATEMATICA
def eh_digito(num):
    for i in range(10):
        if num == str(i):
            return True
    return False

def eh_numero(num):
    ha_nums = False
    ha_um_ponto = False
    primeiro = 0
    if eh_traco(num[0]):
        primeiro = 1
    for i in range(primeiro,length(num)):
        if eh_digito(num[i]):
            ha_nums = True
        elif eh_ponto(num[i]):
            if ha_um_ponto:
                return False
            ha_um_ponto = True
        else:
            return False
    return ha_nums

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

def eh_inteiro(num):
    if (eh_numero(num)) and (not eh_float(num)):
        return True
    return False

def eh_tipo_inteiro(num):
    return(type(num) == int)

def eh_positivo(num):
    return (num > 0)

def eh_negativo(num):
    return (num < 0)

def eh_multiplo(candidato,numero):
    return (candidato % numero == 0)
        

def eh_par(num):
    if num % 2 == 0:
        return True
    return False

def eh_impar(num):
    if num % 2 == 1:
        return True
    return False

def elevar_a_fator(num,fator=2):
    return num ** fator
"""==============================================================================================="""

#3. STRINGS
def split(stringa, separador=' '): #spllit
    new_string = ''
    string = stringa + separador
    lista = []
    for char in string:
        if char != separador:
            new_string += char
        else:
            lista.append(new_string)
            new_string = ''
    return lista

def mapear(funcao,colecao): #map
    if type(colecao) == list:
        lista_modificada = []
        for item in colecao:
            lista_modificada.append(funcao(item))
        return lista_modificada
    elif type(colecao) == str:
        string_modificada = ''
        for char in colecao:
            string_modificada += funcao(char)
        return string_modificada
    '''elif type(colecao) == tuple:
        lista_modificada = []
        for item in colecao:
            lista_modificada.append(funcao(item))
        return tuple(lista_modificada)'''        
    return colecao

def push(vetor,item):
    return vetor + [item]

def popp(vetor):
    x = []
    for i in range(length(vetor) - 1):
        x = push(x,vetor[i])
    return x

def delete(vetor,indice):
    lista = []
    for i in range(length(vetor)):
        if i != indice:
            lista = push(lista,vetor[i])
    return lista

def buscar(lista,item): #in
    for elemento in lista:
        if item == elemento:
            return True
    return False

def filtrar(funcao_criterio,lista): #filter
    filtrados = []
    for item in lista:
        if funcao_criterio(item):
            filtrados = push(filtrados,item)
    return filtrados

def char_para_maiusculo(char):
    if 97 <= ord(char) <= 122:
        return chr(ord(char) - 32)
    return char

def char_para_minusculo(char):
    if 65 <= ord(char) <= 90:
        return chr(ord(char) + 32)
    return char
def palavra_para_maiusculo(string):
    maiusculo = mapear(char_para_maiusculo,string)
    return maiusculo
def palavra_para_minusculo(string):
    minusculo = mapear(char_para_minusculo,string)
    return minusculo

def eh_traco(char):
    return (char == '-')
#def eh_traco(num):
    #return (ord(num) == 45)

def eh_ponto(num):
    return ord(num) == 46
def eh_float(num):
    for char in num:
        if char == '.':
            return True
    return False

def contar_ocorrencias_caractere(texto, caractere_buscado):
    ocorrencias = 0
    for char in texto:
        if char == caractere_buscado:
            ocorrencias += 1
    return ocorrencias

def gerar_randomico(minimo,maximo):
    return randint(minimo,maximo)

def bye():
    lista = ["Adeus, minha pimenta!", "Até mais, meu biscoitinho!", "Tchau, meu docinho de coco!", "Adeus, meu abacate!", "Até a próxima, meu brigadeiro!", "Tchau, meu pão de queijo!", "Adeus, meu bombonzinho!", "Até logo, minha pipoca!", "Tchauzinho, meu sorvetinho!", "Adeus, minha paçoquinha!", "Até mais, meu petit gateau!", "Tchau, meu cupcake!", "Adeus, meu marshmallow!", "Até a próxima, minha gelatina!", "Tchau, meu bolo de cenoura!", "Adeus, minha cocada!", "Até logo, minha torta de limão!", "Tchauzinho, meu suspiro!", "Adeus, meu chiclete!", "Até mais, meu pretzel!", "Tchau, meu nugget!", "Adeus, meu milkshake!", "Até a próxima, meu churros!", "Tchau, minha paçoca!", "Adeus, meu brigadeiro de panela!", "Até logo, minha geléia!", "Tchauzinho, meu crepe!", "Adeus, minha salada de frutas!", "Até mais, meu cheesecake!", "Tchau, meu biscoito da sorte!", "Adeus, meu sushi!", "Até a próxima, meu tempurá!", "Tchau, meu rolinho primavera!", "Adeus, meu macarrão!", "Até logo, meu bacon!", "Tchauzinho, meu frango a passarinho!", "Adeus, meu hambúrguer!", "Até mais, meu cachorro-quente!", "Tchau, minha pizza!", "Adeus, meu sorvete de casquinha!", "Até a próxima, meu milkshake!", "Tchau, meu bolo de chocolate!", "Adeus, meu croissant!", "Até logo, meu pão francês!", "Tchauzinho, meu waffle!", "Adeus, minha tapioca!", "Até mais, meu pão de mel!", "Tchau, meu brownie!", "Adeus, meu mousse!", "Até a próxima, minha geleia de mocotó!", "Tchau, meu macaron!", "Adeus, meu cuscuz!", "Até logo, meu panetone!", "Tchauzinho, meu brigadeiro branco!", "Adeus, minha coxinha!", "Até mais, meu pastel de feira!", "Tchau, minha empadinha!", "Adeus, meu esfiha!", "Até a próxima, meu churros!", "Tchau, meu pão de queijo!", "Adeus, minha tapioca!", "Até logo, minha geléia!", "Tchauzinho, meu brownie!", "Adeus, meu mousse!", "Até mais"]
    return show(lista[gerar_randomico(0,59)])
    
def limpar_tela():
    if os.name == 'posix':  # Para sistemas baseados em Unix (Linux, macOS, etc.)
        os.system('clear')
    elif os.name == 'nt':   # Para sistemas Windows
        os.system('cls')

def pergunta_sim_ou_nao(label='Sim ou Não?'):
    pergunta = palavra_para_maiusculo(obter_texto(f'{label} (S/N)\n>>>'))
    if pergunta == 'S' or pergunta == 'SIM':
        return True
    elif pergunta == 'N' or pergunta == 'NAO':
        return False
    else:
        return pergunta_sim_ou_nao(label)

def soma_vetor(vetor):
    soma = 0
    for item in vetor:
        if eh_numero(f'{item}'):
            soma += item
    return soma

def bubble_sort(vetor_recebido,reverse=False):
    vetor = vetor_recebido[:]
    ha_trocas =False
    for i in range(length(vetor) - 1):
        ha_trocas = False
        for i in range(length(vetor) - 1):
            if vetor[i] > vetor[i+1]:
                atual = vetor[i] 
                proximo = vetor[i+1]
                vetor[i] = proximo
                vetor[i+1] = atual
                ha_trocas = True
        if not ha_trocas:
            break 
    if reverse:
        return inverter_lista(vetor)     
    return vetor 

def inverter_lista(lista_recebida):
    lista_modificada = lista_recebida[:]
    for i in range(length(lista_recebida)):
        lista_modificada[i] = lista_recebida[-(i+1)] 
    return lista_modificada

def float_int_para_int(real):
    inteirinho = ''
    for char in str(real):
        if not eh_ponto(char):
            inteirinho += char
            continue
        return inteiro(inteirinho)
    
def mediana(lista_recebida):
    lista = bubble_sort(lista_recebida)
    tamanho = length(lista)
    if tamanho == 0:
        return None
    elif eh_impar(tamanho):
        mediana = lista[float_int_para_int(((tamanho + 1) / 2) - 1)]#formula da mediana
    elif eh_par(tamanho):
        mediana = ((lista[float_int_para_int((tamanho/2)-1)] + lista[float_int_para_int((tamanho/2))]) / 2)
    return mediana

def media(somatorio,quantidade):
    if somatorio != 0 and quantidade > 0:
        return somatorio / quantidade
    elif somatorio == 0 and quantidade > 0:
        return 0
    return None

def tirar_repetidos(vetor):
    verificados = []
    for i in range(length(vetor) -1):
        if not buscar(verificados,vetor[i]):
            verificados = push(verificados,vetor[i])
    return verificados

def reduce_produto(vetor):
    acumulado = 1
    for item in vetor:
        acumulado *= item
    return acumulado

def length(vetor):
    count = 0
    for _ in vetor:
        count += 1
    return count

def fabrica_eh_multiplo(numero):
    def ehh_multiplo(candidato):
        return candidato % numero == 0
    return ehh_multiplo

