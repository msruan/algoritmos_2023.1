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