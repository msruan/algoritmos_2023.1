#io
#label
def show(label='',sep='',end='\n'): #print/mostrar_texto
    print(label,sep,end)

def mostrar_texto_inline(label='',sep=''): #print na mesma linha
    show(label,sep,end='')

def mostrar_texto_caixa_alta(string=''): 
    show(palavra_para_maiusculo(string))

def mostrar_texto_caixa_baixa(string=''):
    show(palavra_para_minusculo(string))

def obter_texto(label='Digite um texto: '): #input/obter_texto
    texto = input(label)
    if texto == '':
        return obter_texto(label)
    return texto

def obter_resposta_sim_ou_nao(label='Sim ou Não?'):
    pergunta = palavra_para_maiusculo(obter_texto(f'{label} (S/N)\n>>>'))
    if pergunta == 'S' or pergunta == 'SIM':
        return True
    elif pergunta == 'N' or pergunta == 'NAO':
        return False
    else:
        return obter_resposta_sim_ou_nao(label)

def obter_texto_tam_minimo(tamanho_minimo,label=''):#label = aquela mensagemzinha que a gente manda pro input
    if label == '':#a mensagem está vazia?
        texto = obter_texto(f'Por favor, insira um texto de tamanho mínimo {tamanho_minimo}!')
    else:
        texto = obter_texto(label)
    if length(label) < tamanho_minimo:#tá no tamanho adequado?
        return obter_texto_tam_minimo()
    return texto

def obter_texto_tam_maximo(tamanho_maximo,label=''):
    if label == '':#a mensagem está vazia?
        texto = obter_texto(f'Por favor, insira um texto de tamanho mínimo {tamanho_maximo}!')
    else:
        texto = obter_texto(label)
    if length(label) > tamanho_maximo:#tá no tamanho adequado?
        return obter_texto_tam_maximo()
    return texto

def obter_texto_tam_min_maximo(label,tamanho_minimo, tamanho_maximo):
    if label == '':#a mensagem está vazia?
        texto = obter_texto(f'Por favor, insira um texto de tamanho mínimo {tamanho_minimo} e de tamanho máx {tamanho_maximo}!!')
    else:
        texto = obter_texto(label)
    if tamanho_minimo > length(label) or length(label) > tamanho_maximo:
        return obter_texto_tam_min_maximo()
    return texto

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

def obter_inteiro_positivo(label='Digite um inteiro positivo: '):
    numero = obter_numero(label)
    if not(eh_tipo_inteiro and numero > 0):
        return obter_inteiro_positivo(label)
    return numero
    
def obter_inteiro_negativo(label='Insira um inteiro negativo'):
    numero = obter_numero(label)
    if not(eh_tipo_inteiro(numero) and numero < 0):
        return obter_inteiro_positivo(label)
    return numero

def obter_numero_minimo(tamanho_minimo,label=''):
    if label == '':#mensagem vazia?
        num = obter_numero(f'Por favor, digite um número maior ou igual a {tamanho_minimo}: ')
    else:
        num = obter_numero(label)
    if num < tamanho_minimo:
        return obter_numero_minimo(label)
    return num
    
def obter_numero_maximo(tamanho_maximo,label='Insira um número: '):
    if label == '':#mensagem vazia?
        num = obter_numero(f'Por favor, digite um número menor ou igual a {tamanho_maximo}: ')
    else:
        num = obter_numero(label)
    if num > tamanho_maximo:
        return obter_numero_maximo(label)
    return num
    
def obter_numero_faixa(tamanho_minimo, tamanho_maximo,label='Insira um número: '):
    if label == '':#mensagem vazia?
        num = obter_numero(f'Por favor, insira um número de ho mínimo {tamanho_minimo} e de máximo {tamanho_maximo}: ')
    else:
        num = obter_numero(label)
    if tamanho_minimo > num or num > tamanho_maximo:
        return obter_numero_faixa(label)
    return num

def obter_inteiro_minimo(tamanho_minimo,label=''):
    if label == '':#mensagem vazia?
        num = obter_inteiro(f'Por favor, digite um número maior ou igual a {tamanho_minimo}: ')
    else:
        num = obter_inteiro(label)
    if num < tamanho_minimo:
        return obter_inteiro_minimo(label)
    return num
    
def obter_inteiro_maximo(tamanho_maximo,label='Insira um número: '):
    if label == '':#mensagem vazia?
        num = obter_inteiro(f'Por favor, digite um número menor ou igual a {tamanho_maximo}: ')
    else:
        num = obter_inteiro(label)
    if num > tamanho_maximo:
        return obter_inteiro_maximo(label)
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


#arraystring
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
    elif type(colecao) == tuple:
        lista_modificada = []
        for item in colecao:
            lista_modificada.append(funcao(item))
        return tuple(lista_modificada)
    
def filtrar(funcao_criterio,lista): #filter
    filtrados = []
    for item in lista:
        if funcao_criterio(item):
            filtrados = push(filtrados,item)
    return filtrados
    
def length(colecao):
    count = 0
    for _ in colecao:
        count += 1
    return count

def revert(lista_recebida):
    lista_modificada = lista_recebida[:]
    for i in range(length(lista_recebida)):
        lista_modificada[i] = lista_recebida[-(i+1)] 
    return lista_modificada

def buscar(lista,item): #in
    for elemento in lista:
        if item == elemento:
            return True
    return False



#array_utils
def delete(vetor,indice):
    lista = []
    for i in range(length(vetor)):
        if i != indice:
            lista = push(lista,vetor[i])
    return lista

def push(vetor,item):
    return vetor + [item]

def pop(vetor):
    x = []
    for i in range(length(vetor) - 1):
        x = push(x,vetor[i])
    return x

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
        return revert(vetor)     
    return vetor 

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

def soma_vetor(vetor):
    soma = 0
    for item in vetor:
        if eh_numero(f'{item}'):
            soma += item
    return soma

def contar_ocorrencias_numero(lista, numero_buscado):
    ocorrencias = 0
    for item in lista:
        if item == numero_buscado:
            ocorrencias += 1
    return ocorrencias

def mostrar_vetor(vetor):
    vetor_visual = '[ '
    for i in range(length(vetor)):
        vetor_visual += f'{vetor[i]}; '
    show(f'{vetor_visual}]\n')

#string

def split(string, separador=' '): #spllit
    item = ''
    string = string + separador
    lista = []
    for char in string:
        if char != separador:
            item += char
        else:
            lista.append(item)
            item = ''
    return lista

def join(string, separador=' '): #join
    new_string = ''
    for char in string:
         if char != separador:
            new_string += char
    return new_string

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

def eh_ponto(num):
    return ord(num) == 46

def eh_letra(char):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,alfabeto)

def eh_minuscula(char):
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    return buscar(char,minusculas)

def eh_maiuscula(char):
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,maiusculas)

def contar_ocorrencias_caractere(texto, caractere_buscado, ignore_caixa_alta_e_baixa=True):
    ocorrencias = 0
    for char in texto:
        if char == char_para_maiusculo(caractere_buscado) or char == char_para_minusculo(caractere_buscado):
            ocorrencias += 1
    return ocorrencias

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

def float_int_para_int(real):
    inteirinho = ''
    for char in str(real):
        if not eh_ponto(char):
            inteirinho += char
            continue
        return inteiro(inteirinho)

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
    if (eh_numero(num)) and (not eh_float(num)):
        return True
    return False

def eh_tipo_inteiro(num):
    return(type(num) == int)

def eh_par(num):
    if num % 2 == 0:
        return True
    return False

def eh_impar(num):
    if num % 2 == 1:
        return True
    return False

def eh_primo(num):
    if num < 0:
        return False
    if num == 0 or num == 1 or num == 2 or num == 3 or num == 5 or num == 7:
        return True
    elif (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0):
        return False
    return True

def eh_positivo(num):
    return (num > 0)

def eh_negativo(num):
    return (num < 0)

def eh_multiplo(candidato,numero):
    return (candidato % numero == 0)
        

def eh_numero_perfeito(num):
    lista_divisores = divisores(num) 
    del(lista_divisores[-1])
    sum = 0
    for item in lista_divisores:
        sum += item
    return (sum == num)

def fabrica_eh_multiplo(numero):
    def ehh_multiplo(candidato):
        return candidato % numero == 0
    return ehh_multiplo

#math básicas
def mmc(a,b):
    ememc = a
    while not(ememc % b == 0 and ememc % a == 0):
        ememc += 1
    return ememc

def mdc(a,b):
    emedc = a
    while not(a % emedc == 0 and b % emedc == 0):
        emedc -= 1
    return emedc

def media(somatorio,quantidade):
    if somatorio != 0 and quantidade > 0:
        return somatorio / quantidade
    elif somatorio == 0 and quantidade > 0:
        return 0
    return None

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

def fatorial(num):
    if num == 1 or num == 0:
        return 1
    return num * fatorial(num - 1)

def divisores(num):
    lista_divisores = []
    for i in range(1,num+1):
        if num % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def elevar_a_fator(num,fator=2):
    return num ** fator

def raiz_quadrada(num):
    return num ** (1/2)

def raiz_cubica(num):
    return num ** (1/3)

def raiz(num,indice):
    return num ** (1/indice)

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