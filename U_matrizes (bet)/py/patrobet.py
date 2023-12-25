#import sys
#sys.path.append("caminho: exemplo: './utils'")

from bet_utils import *
from bet_features import *

def main():
    SAIR = 0
    PATROBET = colored('PatroBET','light_red',attrs=['blink'])

    bilhetes = []
    ganhadores = []
    numeros_sorteados = []
    escolha = -1
    

    while escolha != SAIR:
        HOUVE_SORTEIO = len(bilhetes) > 0 and len(ganhadores) > 0
        HOUVE_COMPRAS = len(bilhetes) > 0 and len(ganhadores) == 0
        
            
        if HOUVE_SORTEIO:
            escolha = obter_opcao(0,4,gerar_menu(PATROBET,'Resultados loteria, Mostrar arrecadação total, Mostrar tabela de arrecadação, Zerar sistema'))
            RESULTADOS_LOTERIA = 1
            MOSTRAR_ARRECADACAO = 2
            MOSTRAR_TABELA = 3
            ZERAR_SISTEMA = 4
            VENDER_BILHETES = None
            REALIZAR_SORTEIO = None
            
        elif HOUVE_COMPRAS:
            escolha = obter_opcao(0,5,gerar_menu(PATROBET,'Vender Bilhetes, Mostrar arrecadação total, Mostrar tabela de arrecadação, Realizar sorteio, Zerar sistema'))
            VENDER_BILHETES = 1
            MOSTRAR_ARRECADACAO = 2
            MOSTRAR_TABELA = 3
            REALIZAR_SORTEIO = 4
            ZERAR_SISTEMA = 5
            RESULTADOS_LOTERIA = None
            
        else:
            escolha = obter_opcao(0,1,gerar_menu(PATROBET,'Vender Bilhetes'))
            VENDER_BILHETES = 1
            MOSTRAR_ARRECADACAO = None
            MOSTRAR_TABELA = None
            REALIZAR_SORTEIO = None
            ZERAR_SISTEMA = None
            RESULTADOS_LOTERIA = None
        
        if escolha == VENDER_BILHETES:
            bilhetes = vender_bilhetes(bilhetes)
        
        elif escolha == ZERAR_SISTEMA:
            bilhetes = []
            ganhadores = []

        elif escolha == MOSTRAR_ARRECADACAO:
            show(arrecadacao_total(bilhetes))
            
        elif escolha == MOSTRAR_TABELA:
            show(tabela_arrecadacao(bilhetes))

        elif escolha == REALIZAR_SORTEIO:
            if len(bilhetes) > 0:
                sorteio = realizar_sorteio(bilhetes)
                numeros_sorteados = sorteio[0]
                ganhadores = sorteio [1]

        elif escolha == RESULTADOS_LOTERIA:
            mostrar_sub_resultados(ganhadores,numeros_sorteados)

        enter_limpar_tela()
    bye()

main()