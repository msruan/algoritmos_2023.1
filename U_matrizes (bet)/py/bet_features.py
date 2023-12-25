from time import sleep
from random import randint
from bet_utils import *   
from termcolor import colored 

#1
def vender_bilhetes(bilhetes_recebidos):
    show(titulo("VENDA DE BILHETES"),'\n')
    bilhetes = bilhetes_recebidos[:]
    quantidade = obter_inteiro_positivo("Quantos bilhetes? ")
    while obter_resposta_s_ou_n('\nDeseja escolher seus números? '):
        bilhetes.append(venda_manual())
        quantidade -= 1
        if not quantidade:
            break
    if quantidade:
        show("\nGerando",colored("...",attrs=["blink"]))
        for _ in range(quantidade):
            bilhetes.append(gerar_surpresinha())
    limpar_tela()
    show(titulo("VENDA DE BILHETES"),'\n')
    show(f'\n{colored(str(len(bilhetes)),"yellow")} bilhetes gerados com sucesso!\n')
    if obter_resposta_s_ou_n('Deseja listá-los?'):
        for bilhete in bilhetes:
            show(mostrar_bilhete(bilhete),'\n')
    show('\n')
    return bilhetes

def venda_manual():
    novo_bilhete = obter_texto('Digite os números de sua preferência separados por um espaço!\nExemplo:\n1 2 3 4 5 6\n\n>>>')
    novo_bilhete = split(novo_bilhete)
    novo_bilhete = mapear(int,novo_bilhete)
    if len(novo_bilhete) > 6 or len(novo_bilhete) < 4:
        show('Confira suas entradas!')
        return venda_manual()
    for numero in novo_bilhete:
        if numero not in [x for x in range(1,61)]:
            show(f'Número {numero} é inválido!')
            return venda_manual()
    return bubble_sort(novo_bilhete)

def gerar_surpresinha():
    bilhete = []
    while len(bilhete) < 6:
        numero_aleatorio = obter_dezena_valida()
        if numero_aleatorio not in bilhete:
            bilhete.append(numero_aleatorio)
    return bubble_sort(bilhete)

#2
def arrecadacao_total(bilhetes):
    
    arrecadacao = f'''
    {titulo("ARRECADACÃO TOTAL")}
    O total de dinheiro arrecadado foi R$ {colored(str(len(bilhetes) * 4.5),"green")}.'''
    return arrecadacao

def titulo(texto):
    return "============ "+colored(texto,"red",attrs=["blink"])+" ============"

#3
def tabela_arrecadacao(bilhetes):
    total = len(bilhetes) * 4.5
    return f'''
{titulo("TABELA DE ARRECADAÇÃO")} 
|Total  > R${colored(str(total),"green")}
|Prêmio bruto  > R${colored(str(0.4335*total),"green")}
|
|Seguridade Social  > R${colored(str(.1732*total),"green")}
|Fundo Nacional da Cultura - FNC  > R${colored(str(.0292*total),"green")}
|Fundo Penitenciário Nacional - FUNPEN  > R${colored(str(0.01*total),"green")}
|Fundo Nacional de Segurança Pública - FNSP	 > R${colored(str(.0926*total),"green")}
|Ministério do Esporte (Ministério da Cidadania)  > R${colored(str(0.246*total),"green")}
|Fenaclubes  > R${colored(str(.0001*total),"green")}
|Secretarias de esporte, ou órgãos equivalentes, dos Estados e do Distrito Federa  > R${colored(str(0.01*total),"green")}
|Comitê Brasileiro de Clubes - CBC  > R${colored(str(.0046*total),"green")}
|Comitê Brasileiro de Clubes Paralímpicos - CBCP  > R${colored(str(.0007*total),"green")}
|Confederação Brasileira do Desporto Escolar - CBDE	 > R${colored(str(.0022*total),"green")}
|Confederação Brasileira do Desporto Universitário - CBDU  > R${colored(str(.0011*total),"green")}
|Comitê Olímpico do Brasil - COB  > R${colored(str(.0173*total),"green")}
|Comitê Paralímpico Brasileiro - CPB  > R${colored(str(.0096*total),"green")}
=================================================
|Despesas de custeio e manutenção:  > R${colored(str(0.1913*total),"green")}
|Comissão dos lotéricos -  > R${colored(str(.0861*total),"green")}
|*Comissão dos lotéricos referente às vendas nos Canais Eletrônico  > R${colored(str(0.04*total),"green")}​
|Custeio de despesas operacionais -  > R${colored(str(.0957*total),"green")}
|Fundo de Desenvolvimento de Loterias - FDL -  > R${colored(str(.0095*total),"green")}	
=================================================\n'''
    
#4
def realizar_sorteio(bilhetes):
    sorteados = []
    senas = []
    quinas = []
    quadras = []
    while True:
        escolhido = gerar_randomico(1,60)
        if escolhido in sorteados:
            continue
        sorteados.append(escolhido)        
        limpar_tela()
        show(titulo("SORTEIO"))
        show(f"{interjeicao()} O número sorteado foi {colored(str(escolhido),'blue')}!\n")
        
        if (len(sorteados) == 6):
            sleep(2)
            break
        
        show(f"\nSorteando o próximo{colored('...',attrs=['blink'])}")
        sleep(3)
                
    for bilhete in bilhetes:
        acertos = 0
        for numero in bilhete:
            if numero in sorteados:
                acertos += 1
        if acertos == 4:
            quadras += [bilhete]
        elif acertos == 5:
            quinas += [bilhete]
        elif acertos == 6:
            senas += [bilhete]
    
    limpar_tela()
    show(titulo("SORTEIO"),'\n')
    '''
    colorir_ciano = lambda x: colored(str(x),"cyan")
    sorteados_coloridos = mapear(colorir_ciano,sorteados)
    '''
    show(f"Números premiados: {mostrar_bilhete(sorteados)}",'\n')
    
    show(f'Houve {len(senas)} quadras premiadas!') if len(senas) else show("ACUMULOU!!!!")
    show(f'Houve {len(quinas)} quinas premiadas!') if len(quinas) else show("Não houve quinas premiadas!")
    show(f'Houve {len(quadras)} quadras premiadas!') if len(quadras) else show("Não houve quadras premiadas!")
    
    return [sorteados,[quadras,quinas,senas]]

def obter_dezena_valida():
    return randint(1, 60)

#5
def mostrar_sub_resultados(ganhadores,numeros_sorteados):
    quadras = ganhadores[0]
    quinas = ganhadores[1]
    senas = ganhadores[2]

    MOSTRAR_QUADRAS = 1
    MOSTRAR_QUINAS = 2
    MOSTRAR_SENAS = 3
    SAIR = 0
    opcao = -1
    menu = gerar_menu(f'{titulo("GANHADORES")}','Mostrar Quadras, Mostrar Quinas, Mostrar Senas')
    while opcao != SAIR:
        limpar_tela()
        if opcao == MOSTRAR_QUADRAS:
            show(titulo('MOSTRAR QUADRAS'))
            show("\n")
            if len(quadras) > 0:
                for bilhete in quadras:
                    show(mostrar_sorteados_no_bilhete(bilhete,numeros_sorteados),'\n')
                show(f'Há {len(quadras)} quadras ganhadoras!')
            else:
                nao_ha_ganhadores()
            enter_limpar_tela()

        elif opcao == MOSTRAR_QUINAS:
            show(titulo('MOSTRAR QUINAS'))
            if len(quinas) > 0:
                for bilhete in quadras:
                    show(mostrar_sorteados_no_bilhete(bilhete,numeros_sorteados),'\n')
                show(f'Há {len(quinas)} quinas!')
            else:
                nao_ha_ganhadores()
            enter_limpar_tela()

        elif opcao == MOSTRAR_SENAS:
            show(titulo('MOSTRAR SENAS'))
            if len(senas) > 0:
                for bilhete in senas:
                    show(mostrar_sorteados_no_bilhete(bilhete,numeros_sorteados),'\n')
                show(f'Há {len(senas)} senas!')
            else:
                nao_ha_ganhadores()
            enter_limpar_tela()
                
        opcao = obter_opcao(0,3,menu)

def gerar_menu(titulo,opcoes_recebidas):
    opcoes = split_especifico(opcoes_recebidas,',')
    menu = f'=============== {titulo} ===============\n'
    for i in range(len(opcoes)):
        menu += f'| {i+1} - {opcoes[i]}\n'
    saida = '| 0 - Sair\n=======================================\n\n>>> '
    return menu + saida

def nao_ha_ganhadores():
    show('Não há ganhadores nesta categoria!')

def split_especifico(string, separador=' '): #spllit
    item = ''
    string = ' ' + string + separador
    lista = []
    for char in string:
        if char != separador:
            item += char
        else:
            lista.append(item)
            item = ''
    return mapear(fabrica_remover_caractere_index(0),lista)
#consertar posteriormente e fazer um split para dois caracteres

def fabrica_remover_caractere_index(index):
    def remover_caractere_index(string):
        nova_string = ''
        for i in range(len(string)):
            if i != index:
                nova_string += string[i]
        return nova_string
    return remover_caractere_index

#extra
'''
def show_bilhetes(bilhetes):
    show("Bilhetes PatroBET")
    # TO FIX
    bilhetes = bubble_sort(bilhetes, lambda b: sum(b), 0)
    if len(bilhetes) < 1:
        # Empty State
        show("Não há bilhetes ainda")
        return
    mostrar_matriz(bilhetes)

def ler_database():
    # check modes ('a', 'r', etc)
    arquivo = open('arquivo.txt', 'r')

    linhas = arquivo.readlines()

    # clean lines
    linhas = map(str.strip, linhas)

    for linha in linhas:
        print(linha)

    arquivo.close()
    return linhas
'''

''' 
def vender_ponto(disponiveis,comprados):
    if len(disponiveis) > 0:
        quer_escolher = obter_resposta_s_ou_n('Deseja escolher seu ponto? ')
        if quer_escolher:
            escolhido = 0
            while not buscar(disponiveis,escolhido):
                show("Pontos disponíveis:")
                linhas = ler_database()
                disponiveis = []
                count_linha = 0
                for linha in linhas:
                    if linha[0] != '-':
                        show(linha,end='')
                        disponiveis += [count_linha]
                obter_texto('Escolha um ponto disponível na tabela acima: ')
            nome = obter_texto("Digite seu nome: ")
            nova_disponivel = []
            for ponto in disponiveis:
                if ponto == escolhido:
                    continue
                nova_disponivel += [ponto]
            disponiveis = nova_disponivel
        elif not quer_escolher:
            escolhido = gerar_randomico(0,len(disponiveis)-1)
            disponiveis = delete(disponiveis,escolhido)
        comprados += [escolhido]
        #escrever ponto no arquivo
'''