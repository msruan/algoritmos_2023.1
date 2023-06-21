from rifa_utils import *
from rifa_features import *
from time import sleep
#arrecadacao ta errada. a tela nao ta limpando quando uma opcao é escolhida
def main():
    #GERAR_RIFA = 1
    #VENDA_PONTO = 2
    MOSTRAR_RIFA = 1
    SORTEIO = 2
    SET_PREMIOS = 3
    SET_PRECO_RIFA = 4
    SET_TAXA_ADM = 5
    CALCULAR_RECEITA = 6
    RESET = 7
    EXIT = 0
    preco = 4.5
    taxa_adm = 0.1
    '''quantidade_de_pontos = obter_inteiro_minimo(2,'Digite o número de pontos que a rifa vai ter: ')
    for i in range(quantidade_de_pontos):
        escrever_linha(f'-{i}')
        pontos += [0]'''
    premios = ['um PatroPhone']
    pontos = inicializacao()
    while True:
        show(menu())
        opcao = obter_inteiro_faixa(0,9,'Digite a opção desejada: ')
        limpar_tela()
        if opcao == EXIT:
            return bye()
        print("*"*50,'\n')
        '''if opcao == GERAR_RIFA:
            pass
        elif opcao == VENDA_PONTO:
            pass'''
        if opcao == MOSTRAR_RIFA:
            show(mostrar_rifa(pontos))
        elif opcao == SORTEIO:
            realizar_sorteio(pontos,premios)
        elif opcao == SET_PREMIOS:
            premios = acrescentar_premios(premios)
        elif opcao == SET_PRECO_RIFA:
            preco = mudar_preco_rifa()
        elif opcao == SET_TAXA_ADM:
            taxa_adm = mudar_taxa_administracao()
        elif opcao == CALCULAR_RECEITA:
            show(calcular_arrecadacao(preco,taxa_adm,pontos))
        
        elif opcao == RESET:
            tem_certeza = obter_resposta_sim_ou_nao('AVISO: Você apagará toda a base de dados!\nTem certeza que deseja continuar? ')
            if tem_certeza:
                resetar_database()
                return main()
        print('\n',"*"*50)
        print()
        input('Pressione ENTER para continuar...')
        sleep(0.5)
        limpar_tela()

def menu():
    return '''\n

/ ========== PatroRIFA ============\\
| 1. Mostrar informações da rifa    |
| 2. Sorteio                        |
| 3. Setar prêmios                  |
| 4. Setar preço da rifa            |
| 5. Setar taxa de administração    |
| 6. Calcular receita total         |
| 7. Resetar sistema                |
| 0. Sair                           |
\ ================================= /
'''  

def inicializacao():
    arquivo = open('rifa_database.txt', 'r')
    linhas = arquivo.readlines()
    # clean lines
    linhas = map(str.strip, linhas)
    dicionario = {}
    count_linha = 1
    for linha in linhas:
        if linha[0] != '-':
            dicionario[f'{count_linha}'] = linha
        else:
            dicionario[f'{count_linha}'] = ''
        count_linha += 1
    return dicionario
    


main()