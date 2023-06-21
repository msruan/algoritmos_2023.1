from time import sleep
from random import randint
from my_utils.my_io_utils import *
from my_utils.my_arraystring_utils import *
from my_utils.my_array_utils import *
from my_utils.my_math_utils import *
from my_utils.my_strings_utils import *

def main():
    bilhetes = []
    venda_manual(bilhetes)
    opcao = obter_numero(menu())
    bilhetes = []
    while opcao != 0:
        show(f"Você escolheu a opção {opcao}")

        if opcao == 1:
            vender_bilhetes(bilhetes)
        if opcao == 2:
            show(arrecadacao_total(bilhetes))
        elif opcao == 10:
            show_bilhetes(bilhetes)
        input('Enter.. ?')
        limpar_tela()
        opcao = obter_numero(menu())
    bye()


def menu():
    opcoes = "###### PatroBET ######"
    opcoes += "\n1 - Vender Bilhete(s)"
    opcoes += "\n2 - Mostrar valor arrecadado!"
    opcoes += "\n10 - Mostrar Bilhetes PatroBet"
    opcoes += "\n0 - Sair"
    opcoes += "\n\n>>>: "

    return opcoes


def vender_bilhetes(bilhetes):
    quantidade = obter_inteiro_positivo("Quantos bilhetes? ")

    for _ in range(quantidade):
        escolher_seus_numeros = obter_resposta_sim_ou_nao('Deseja escolher seus números? ')
        if escolher_seus_numeros:
            novo_bilhete = venda_manual()
        elif not escolher_seus_numeros:
            novo_bilhete = gerar_surpresinha()
        bilhetes.append(novo_bilhete)
        show(f'O bilhete escolhido foi {novo_bilhete}.\n\n')
        input('Enter...?')
        limpar_tela()
    show(f"{quantidade} bilhetes gerados com sucesso!")

def venda_manual():
    novo_bilhete = map(int,input('Digite os números de sua preferência separados por um espaço!\nExemplo:\n1 2 3 4 5 6\n\n>>>').split())
    for numero in novo_bilhete:
        if numero not in [x for x in range(1,61)] or len(novo_bilhete) > 6 or len(novo_bilhete) < 4:
            return limpar_tela() or print('Confira sua entrada!\n') or venda_manual()
    return novo_bilhete

def gerar_surpresinha():
    bilhete = []
    while len(bilhete) < 6:
        numero_aleatorio = obter_dezena_valida()
        if numero_aleatorio not in bilhete:
            bilhete.append(numero_aleatorio)

    return bubble_sort(bilhete)

def arrecadacao_total(bilhetes):
    arrecadacao = f'O total de dinheiro arrecadado foi R$ {len(bilhetes) * 4.5}.' if len(bilhetes) > 0 else 'Ainda não foram vendidos bilhetes!'
    return arrecadacao

def obter_dezena_valida():
    return randint(1, 60)

def realizar_sorteio(bilhetes):
    sorteados = []
    hexas = []
    quinas = []
    quadras = []
    escolhido = None
    while len(sorteados) < 6:
        escolhido = gerar_randomico(1,60)
        if escolhido not in sorteados:
            show(f'{escolhido}...')
            sorteados.append(escolhido)
            sleep(3)
    acertos = 0
    for bilhete in bilhetes:
        for item in bilhete:
            if item in sorteados:
                acertos += 1
    if acertos == 4:
        quadras += [bilhete]
    elif acertos == 5:
        quinas += [bilhete]
    elif acertos == 6:
        hexas += [bilhete]
    acertos = 0


def show_bilhetes(bilhetes):
    show("Bilhetes PatroBET")

    # TO FIX
    bilhetes = bubble_sort(bilhetes, lambda b: sum(b), 0)

    if len(bilhetes) < 1:
        # Empty State
        show("Não há bilhetes ainda")
        return

    show_matriz(bilhetes)

def show_matriz(matriz):
    for array in matriz:
        show(array)
        
def show_vetor(vetor):
    show("[")
    for item in vetor:
        show(f'{item}\n',)
    show("]")
'''
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
    if length(disponiveis) > 0:
        quer_escolher = obter_resposta_sim_ou_nao('Deseja escolher seu ponto? ')
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
            escolhido = gerar_randomico(0,length(disponiveis)-1)
            disponiveis = delete(disponiveis,escolhido)
        comprados += [escolhido]
        #escrever ponto no arquivo
'''

main()
