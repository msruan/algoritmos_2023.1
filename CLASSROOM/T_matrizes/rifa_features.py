from rifa_utils import *
from time import sleep
#1
def mostrar_rifa(pontos):
    comprados = []
    disponiveis = []
    for i in range(1,len(pontos)+1):
        if pontos[f'{i}'] != '':
            comprados += [i]
            continue
        disponiveis += [i]
    saida = ''
    saida += f'Quantidade de pontos disponíveis: {len(disponiveis)}\n'
    saida += f'Quantidade de pontos vendidos: {len(comprados)}\n\n'
    saida += f'Pontos disponíveis: {disponiveis}\n'
    saida += f'Pontos vendidos: {comprados}'
    return saida
#2
def realizar_sorteio(pontos,premios):
    comprados = []
    for i in range(1,len(pontos)+1):
        if pontos[f'{i}'] != '':
            comprados += [f'{i}{pontos[f"{i}"]}']
    sorteado = None
    sorteados = []
    for i in range(len(premios)):
        show("Sorteando..")
        sleep(2.5)
        show(f"{interjeicao()} O número sorteado foi..")
        sleep(2)
        sorteado = gerar_randomico(0,len(comprados)-1)
        ganhador = comprados[sorteado]
        numero = ''
        nome = ''
        for char in ganhador:
            if eh_digito(char):
                numero += char
            else:
                nome += char
        show(f"{numero}!!!!!!!")
        sleep(1)
        show(f'Parabéns {nome}, você ganhou {premios[i]}!')
        del comprados[sorteado]
        sorteados += [numero]
        sleep(1.5)
        if len(sorteados) < len(premios):
            limpar_tela()
            print("*"*50,'\n')

#3
def acrescentar_premios(premios_atuais):
    premios = premios_atuais[:]
    show('Lista antiga de prêmios:')
    show(f'{premios}\n')
    quantidade = obter_inteiro_positivo('Quantos prêmios serão rifados?\n\n>> ')
    limpar_tela()
    for _ in range(quantidade):
        premios = push(premios,obter_texto('Diga qual o prêmio!\n\n>>'))
        limpar_tela()
    show('Prêmios adicionados com sucesso!')
    show('Nova lista de prêmios:')
    show(f'{premios}')
    return premios

#4
def mudar_preco_rifa():
    return obter_numero_positivo('Digite o valor da rifa: ')

#5
def mudar_taxa_administracao():
    return obter_numero_positivo('Digite a taxa de administração em %: ') / 100

#6
def calcular_arrecadacao(preco,taxa_administracao,vendidos):
    arrecadacao = 0
    for i in range(1,length(vendidos)+1):
        if vendidos[f'{i}'] != '':
            arrecadacao += preco
    if arrecadacao == 0:
        return 'Nenhum ponto foi vendido ainda!'
    taxa_adm = arrecadacao * taxa_administracao
    liquido = arrecadacao - taxa_adm
    saida = 'RECEITA TOTAL'.center(70, '*')
    saida += f'\nValor da rifa: R${preco}'
    saida += f'\nTaxa de administração: {taxa_administracao*100}%\n'
    saida += f'\nArrecadação bruta: {arrecadacao}'
    saida += f"\nValor líquido: {liquido}"
    saida += f'\nDesconto da adminsitração: {taxa_adm}'
    return saida

#7
def resetar_database():
    database = open('rifa_database.txt', 'w') 
    database.close()