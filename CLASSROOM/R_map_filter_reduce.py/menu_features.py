from my_utils import *

#1
def gerar_vetor():
    vetor_temporario = [obter_valor_padrao()] * obter_inteiro_positivo('Quantas posições terá o vetor? ')
    return vetor_temporario

def obter_valor_padrao():
    pergunta = pergunta_sim_ou_nao('\nDeseja fornecer um valor padrão?')
    if pergunta:
        return obter_numero('\nQual o valor padrão? ')
    else:
        return None
    #else:
        #return obter_valor_padrao()
    
#2
def preencher_vetor_manual(vetor):
    vetor_temporario = vetor[:]
    #uma mapear conceitual
    for i in range(length(vetor_temporario)):
        vetor_temporario[i] = obter_numero('Digite um valor: ')
    return vetor_temporario

#3
def preencher_vetor_auto(vetor_recebido):
    vetor = vetor_recebido[:]
    min = obter_inteiro_positivo('Qual o valor mínimo? ')
    max = obter_inteiro_positivo("Qual o valor máximo? ")
    show(vetor)
    '''Há possibilidade de perguntar pro usuário se ele deseja repetições?
    Verifica-se se o intervalo de escolha de valores aleatórios é menor que o tamanho do vetor.'''
    if length(vetor) > (max - min + 1):
        show('Aviso: Não há como proibir repetições!')
        #mapear
        for i in range(length(vetor)):
            vetor[i] = gerar_randomico(min,max)
        return vetor
    
    repeticoes_estao_proibidas = pergunta_sim_ou_nao('Proibir números repetidos?')
    if repeticoes_estao_proibidas:
        #mapear
        for i in range(length(vetor)):
            aleatorio = gerar_randomico(min,max)
            while buscar(vetor,aleatorio):
                aleatorio = gerar_randomico(min,max)
            vetor[i] = aleatorio
    elif not repeticoes_estao_proibidas:
        #mapear
        for i in range(length(vetor)):
            vetor[i] = gerar_randomico(min,max)
    return vetor

#4
def mostrar_vetor(vetor):
    vetor_visual = '[ '
    for i in range(length(vetor)):
        vetor_visual += f'{vetor[i]}; '
    show(f'{vetor_visual}]\n')

#5
def elevar_vetor(vetor_recebido):
    vetor = vetor_recebido[:]
    fator = obter_inteiro_minimo(1,'Qual o fator desejado? ')
    vetor_de_saida = mapear(fabrica_de_elevar_a_fator(fator),vetor)
    return vetor_de_saida

def fabrica_de_elevar_a_fator(fator):
    def filha(num):
        return (num ** fator)
    return filha
88
#6
def dividir_em_positivos_negativos_zeros(vetor):
    positivos = filtrar(eh_positivo,vetor)
    negativos = filtrar(eh_negativo,vetor)
    zeros = filtrar(lambda x: x == 0,vetor)
    return [positivos,negativos,zeros]

def tem_algo_em(x):
    return (length(x) > 0)
def contadora_de_numeros(vetor):
    conjuntos = dividir_em_positivos_negativos_zeros(vetor)
    positivos = conjuntos[0]
    negativos = conjuntos[1]
    zeros = conjuntos[2]
    show(f'Há {length(positivos)} números positivos.')
    show(f'Há {length(negativos)} números negativos.')
    show(f'Há {length(zeros)} zeros.')
    if tem_algo_em(positivos) or tem_algo_em(negativos):
        if pergunta_sim_ou_nao('Deseja listar esse(s) conjunto(s)? '):
            if length(positivos) > 0:
                show('Positivos:')
                mostrar_vetor(positivos)
            if length(negativos) > 0:
                show('Negativos:')
                mostrar_vetor(negativos)
    return None

#7
def mostrar_somatorio(vetor_recebido):
    vetor = dividir_em_positivos_negativos_zeros(vetor_recebido)
    show(f'Soma de todos os números: {soma_vetor(vetor_recebido)}')
    show(f'Soma dos números positivos: {soma_vetor(vetor[0])}')
    show(f'Soma dos números negativos: {soma_vetor(vetor[1])}')
    return None

#8
#a melhorar: média dá valores certos, porém quebrados. uma possivel solução seria incrementar a funcao inteiro para identificar casos em que o numero é inteiro mas está em float automaticamente.
def exibir_media_e_mediana(vetor):
    vetor_divido = dividir_em_positivos_negativos_zeros(vetor)
    positivos = vetor_divido[0]
    negativos = vetor_divido[1]
    limpar_tela()
    show(f'Vetor completo:')
    show(f'Média: {media(soma_vetor(vetor),length(vetor))}.')
    show(f'Mediana: {mediana(vetor)}\n')
    if tem_algo_em(positivos):
        show(f'Positivos:')
        show(f'Média: {media(soma_vetor(positivos),length(positivos))}.')
        show(f'Mediana: {mediana(positivos)}\n')
    if tem_algo_em(negativos):
        show(f'Negativos:')
        show(f'Média: {media(soma_vetor(negativos),length(negativos))}.')
        show(f'Mediana: {mediana(negativos)}\n')
    return None

#9
def maior_menor_numero(vetor):
    vetor_ordenado = bubble_sort(vetor)
    if tem_algo_em(vetor_ordenado):
        show(f'O maior número é {vetor_ordenado[-1]}')
        show(f'O menor número é {vetor_ordenado[0]}')
    return None

#10
def sorteio_positivo_negativo(vetor):
    vetor_dividido = dividir_em_positivos_negativos_zeros(vetor)
    positivos = vetor_dividido[0]
    negativos = vetor_dividido[1]
    sorteados = ''
    if tem_algo_em(positivos):
        index_positivo_sorteado = gerar_randomico(0,length(positivos)-1)
        sorteados += f'O número positivo sorteado foi {positivos[index_positivo_sorteado]}.\n'
    if tem_algo_em(negativos):
        index_negativo_sorteado = gerar_randomico(0,length(negativos)-1)
        sorteados += f'O número negativo sorteado foi {negativos[index_negativo_sorteado]}.\n'
    elif not tem_algo_em(positivos) and not tem_algo_em(negativos):
        return "Não houve números sorteados. Não há números positivos, nem negativos."
    return sorteados

#11
def gerar_n_grupos_tamanho_t(vetor_recebido):
    n = obter_inteiro_positivo('Quantos grupos você quer? ')
    t = n = obter_inteiro_positivo('Qual tamanho você deseja? ')
    vetor = tirar_repetidos(vetor_recebido)
    if t > length(vetor):
        return None
    grupos = []
    if n * t <= length(vetor):
        for _ in range(n):
            grupos = push(grupos,[])
        for grupo in grupos:
            for _ in range(t):
                grupo = push(grupo,vetor[0])
                vetor = delete(vetor,0)
            mostrar_vetor(grupo)
    elif t * n > length(vetor):
        count = 0
        acumulado = 0
        while t + acumulado <= length(vetor):
            count += 1
            acumulado += t
    
        for _ in range(count):
            grupos = push(grupos,[])
        for grupo in grupos:
            for _ in range(t):
                grupo = push(grupo,vetor[0])
                vetor = delete(vetor,0)
            mostrar_vetor(grupo)
    return None       

#12
def vetor_igual_ao_atual(vetor_atual):
    qualquer_ordem = pergunta_sim_ou_nao('Em qualquer ordem? ')
    vetor_pedido = obter_texto('Digite os números do vetor separados por vírgulas: \n>>>>')
    string_splitada = split(vetor_pedido,',')
    vetor_numerico = mapear(number,string_splitada)
    if qualquer_ordem:
        vetor_ordenado = bubble_sort(vetor_numerico)
        return (bubble_sort(vetor_atual) == vetor_ordenado)
    return vetor_atual == vetor_numerico

#13
def top_n_maiores_numeros(vetor):
    n = obter_inteiro_positivo("Quantos maiores números você deseja mostrar? ")
    vetor_ordenado_nao_repetido = tirar_repetidos(bubble_sort(vetor,True))
    maiores = ''
    for i in range(length(vetor_ordenado_nao_repetido)):
        maiores += f'{i+1}º: {vetor_ordenado_nao_repetido[i]};\n'
        if i+1 == n:
            break  
    quantos_nums_no_ranking = contar_ocorrencias_caractere(maiores,";")
    return f'==== Top {quantos_nums_no_ranking} maiores números ====\n' + maiores

#eventuais melhorias: mostrar o ranking no formato 01. tirar o break do for

#14
def top_n_menores_numeros(vetor):
    n = obter_inteiro_positivo("Quantos menores números você deseja mostrar? ") 
    vetor_ordenado_nao_repetido = tirar_repetidos(bubble_sort(vetor))
    menores = ''
    for i in range(length(vetor_ordenado_nao_repetido)):
        menores += f'{i+1}º: {vetor_ordenado_nao_repetido[i]};\n'
        if i+1 == n:
            break  
    quantos_nums_no_ranking = contar_ocorrencias_caractere(menores,";")
    return f'==== Top {quantos_nums_no_ranking} menores números ====\n' + menores

#15
def maiores_menores_que_a_media(vetor):
    a_media = media(soma_vetor(vetor),length(vetor))
    maiores = filtrar(lambda x: x > a_media,vetor)
    menores = filtrar(lambda x: x < a_media,vetor)
    show(f"A média é de {a_media}.")
    if tem_algo_em(maiores):
        show("Maiores que a média: ")
        mostrar_vetor(maiores)
    if tem_algo_em(menores):
        show("Menores que a média: ")
        mostrar_vetor(menores)
    else:
        show('Não há valores diferentes da média!')
    return None

#16
def chatinha(vetor):
    divididos = dividir_em_positivos_negativos_zeros(vetor)
    positivos = divididos[0]
    negativos = divididos[1]
    positivos_multiplos_de_dois = filtrar(fabrica_eh_multiplo(2),positivos)
    a_media_positivos = media(soma_vetor(positivos_multiplos_de_dois),length(positivos_multiplos_de_dois))
    negativos_pares = filtrar(eh_par,negativos)
    negativos_pares_reduzidos_a_metade = mapear(lambda x: x/2,negativos_pares)
    o_produto_negativos = reduce_produto(negativos_pares_reduzidos_a_metade)
    return a_media_positivos + o_produto_negativos

#17
def ordenar_crescente_condicional(vetor):
    divididos = dividir_em_positivos_negativos_zeros(vetor)
    limpar_tela()
    texto = '''
 ========== Quer ordenar... =============
|01. Todes
|02. Pares
|03. Ímpares
|04. Positivos
|05. Negativos
|06. Múltiplos de N
 =========================================
 
 >>>>
    '''
    pergunta = obter_inteiro_faixa(0,5,texto)
    if pergunta == 1:
        return bubble_sort(vetor)
    if pergunta == 2:
        return bubble_sort(filtrar(eh_par,vetor))
    if pergunta == 3:
        return bubble_sort(filtrar(eh_impar,vetor))
    if pergunta == 4:
        return bubble_sort(divididos[0])
    if pergunta == 5:
        return bubble_sort(divididos[1])
    if pergunta == 6:
        n = obter_inteiro('Qual o valor de N? ')
        return bubble_sort(filtrar(fabrica_eh_multiplo(n),vetor))

#18
def ordenar_decrescente_condicional(vetor):
    divididos = dividir_em_positivos_negativos_zeros(vetor)
    limpar_tela()
    texto = '''
 ========== Quer ordenar... =============
|01. Todes
|02. Pares
|03. Ímpares
|04. Positivos
|05. Negativos
|06. Múltiplos de N\n
 ========================================

>>>>>
    '''
    pergunta = obter_inteiro_faixa(0,5,texto)
    if pergunta == 1:
        return bubble_sort(vetor,True)
    if pergunta == 2:
        return bubble_sort(filtrar(eh_par,vetor),True)
    if pergunta == 3:
        return bubble_sort(filtrar(eh_impar,vetor),True)
    if pergunta == 4:
        return bubble_sort(divididos[0],True)
    if pergunta == 5:
        return bubble_sort(divididos[1],True)
    if pergunta == 6:
        n = obter_inteiro('Qual o valor de N? ')
        return bubble_sort(filtrar(fabrica_eh_multiplo(n),vetor),True)
    
#19
def tirar_multplos_de_n_e_m(vetor_recebido):
    vetor_verificado = []
    n = obter_inteiro('Digite o valor de n: ')
    m = obter_inteiro('Digite o valor de m: ')
    a_remover = filtrar(fabrica_eh_multiplo(n*m),vetor_recebido)
    for item in vetor_recebido:
        if not buscar(a_remover,item):
            vetor_verificado = push(vetor_verificado,item)
    return vetor_verificado
