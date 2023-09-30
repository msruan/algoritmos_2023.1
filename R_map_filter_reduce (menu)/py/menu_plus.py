from my_utils import *
from menu_features import *
def main():
    nums = [] 
    opcao = -1
    ha_vetor = False
    nao_ha_nones = False
    while opcao != 0:
        show(menu(ha_vetor,nao_ha_nones))
        opcao = obter_inteiro_faixa(0,19,'Digite a opção desejada: ')

        if opcao == 0:
            break

        elif opcao == 1:
            if ha_vetor:
                nums = []
                nao_ha_nones = False
            elif not ha_vetor:
                nums = gerar_vetor()
                ha_vetor = True

        elif ha_vetor:
            if opcao == 2:
                nums = preencher_vetor_manual(nums)
                nao_ha_nones = True

            elif opcao == 3:
                nums = preencher_vetor_auto(nums)
                nao_ha_nones = True

            elif opcao == 4:
                mostrar_vetor(nums)

            elif nao_ha_nones:

                if opcao == 5:
                    nums = elevar_vetor(nums)

                elif opcao == 6:
                    contadora_de_numeros(nums)

                elif opcao == 7:
                    mostrar_somatorio(nums)

                elif opcao == 8:
                    exibir_media_e_mediana(nums)

                elif opcao == 9:
                    maior_menor_numero(nums)

                elif opcao == 10:
                    show(sorteio_positivo_negativo(nums))

                elif opcao == 11:
                    gerar_n_grupos_tamanho_t(nums)

                elif opcao == 12:
                    show(vetor_igual_ao_atual(nums))

                elif opcao == 13:
                    show(top_n_maiores_numeros(nums))

                elif opcao == 14:
                    show(top_n_menores_numeros(nums))

                elif opcao == 15:
                    maiores_menores_que_a_media(nums)

                elif opcao == 16:
                    show(chatinha(nums))

                elif opcao == 17:
                    nums = ordenar_crescente_condicional(nums)

                elif opcao == 18:
                    nums = ordenar_decrescente_condicional(nums)

                elif opcao == 19:
                    nums = tirar_multplos_de_n_e_m(nums)

        input('\nEnter?')
        limpar_tela()
    limpar_tela()
    bye() 
        
def menu(ja_ha_vetor,nao_ha_nones):
    if not ja_ha_vetor:
        return '''
=========================    MENU     ==================================
1. Gerar vetor N posições
00. Sair
========================================================================
        \n '''
    if ja_ha_vetor:
        menu = '''\n
===================================    MENU     ===================================================
01. Limpar vetor
02. Preencher vetor manualmente item a item
03. Preencher vetor automaticamente'''
    if nao_ha_nones:
        menu += '''
04. Mostrar vetor
05. Transformar vetor: elevar a potência N
06. Contar: Positivos, Negativos e Zeros
07. Somatório: De todos, Dos Negativos e dos Positivos
08. Exibir Média e Mediana: De Todos, Dos Positivos e Dos Negativos
09. Exibir Maior e Menor número
10. Sortear dois números: um positivo e um negativo
11. Gerar N grupos de T tamanhos. Não repetir valores
12. Pedir um novo vetor e verificar se está 100% presente nos números do sistema (e na mesma ordem)
13. Top N maiores números
14. Top N menores números
15. Listar valor médio, e listar números maiores que a Média e Menores que a Média
16. Soma da Média dos Números Positivos Múltiplos De dois COM
   o Produto acumulado dos números negativos pares reduzidos à metade.
17. Ordenar os números em ordem crescente:
18. Ordenar os números em ordem decrescente
19. Eliminar números múltiplos de N e M (simultaneamente)'''
    final = '''
00. Sair
========================================================================
    '''
    return menu + final
    
main() 