from my_strings_utils import palavra_para_maiusculo, palavra_para_minusculo, eh_numero
from my_array_utils import length
from my_math_utils import eh_tipo_inteiro, number, gerar_randomico
import os
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
def bye():
    lista = ["Adeus, minha pimenta!", "Até mais, meu biscoitinho!", "Tchau, meu docinho de coco!", "Adeus, meu abacate!", "Até a próxima, meu brigadeiro!", "Tchau, meu pão de queijo!", "Adeus, meu bombonzinho!", "Até logo, minha pipoca!", "Tchauzinho, meu sorvetinho!", "Adeus, minha paçoquinha!", "Até mais, meu petit gateau!", "Tchau, meu cupcake!", "Adeus, meu marshmallow!", "Até a próxima, minha gelatina!", "Tchau, meu bolo de cenoura!", "Adeus, minha cocada!", "Até logo, minha torta de limão!", "Tchauzinho, meu suspiro!", "Adeus, meu chiclete!", "Até mais, meu pretzel!", "Tchau, meu nugget!", "Adeus, meu milkshake!", "Até a próxima, meu churros!", "Tchau, minha paçoca!", "Adeus, meu brigadeiro de panela!", "Até logo, minha geléia!", "Tchauzinho, meu crepe!", "Adeus, minha salada de frutas!", "Até mais, meu cheesecake!", "Tchau, meu biscoito da sorte!", "Adeus, meu sushi!", "Até a próxima, meu tempurá!", "Tchau, meu rolinho primavera!", "Adeus, meu macarrão!", "Até logo, meu bacon!", "Tchauzinho, meu frango a passarinho!", "Adeus, meu hambúrguer!", "Até mais, meu cachorro-quente!", "Tchau, minha pizza!", "Adeus, meu sorvete de casquinha!", "Até a próxima, meu milkshake!", "Tchau, meu bolo de chocolate!", "Adeus, meu croissant!", "Até logo, meu pão francês!", "Tchauzinho, meu waffle!", "Adeus, minha tapioca!", "Até mais, meu pão de mel!", "Tchau, meu brownie!", "Adeus, meu mousse!", "Até a próxima, minha geleia de mocotó!", "Tchau, meu macaron!", "Adeus, meu cuscuz!", "Até logo, meu panetone!", "Tchauzinho, meu brigadeiro branco!", "Adeus, minha coxinha!", "Até mais, meu pastel de feira!", "Tchau, minha empadinha!", "Adeus, meu esfiha!", "Até a próxima, meu churros!", "Tchau, meu pão de queijo!", "Adeus, minha tapioca!", "Até logo, minha geléia!", "Tchauzinho, meu brownie!", "Adeus, meu mousse!", "Até mais"]
    return show(lista[gerar_randomico(0,59)])

def limpar_tela():
    if os.name == 'posix':  # Para sistemas baseados em Unix (Linux, macOS, etc.)
        os.system('clear')
    elif os.name == 'nt':   # Para sistemas Windows
        os.system('cls')
