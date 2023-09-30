from my_utils import *
from menu_features import *
def main():
    nums = [] 
    opcao = -1
    while opcao != 0:
        show(menu())
        opcao = obter_inteiro_faixa(0,19,'Digite a opção desejada: ')

        if opcao == 1:
            nums = gerar_vetor()

        elif opcao == 2:
            nums = preencher_vetor_manual(nums)

        elif opcao == 3:
            nums = preencher_vetor_auto(nums)

        elif opcao == 4:
            mostrar_vetor(nums)

        elif opcao == 5:
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

        elif opcao == 0:
            break
        input('\nEnter?')
        limpar_tela()
    limpar_tela()
    bye() 
        
def menu():
    return '''\n
 ===================================    MENU     ===================================================
| 01. Gerar vetor N posições
| 02. Preencher vetor manualmente item a item
| 03. Preencher vetor automaticamente
| 04. Mostrar vetor
| 05. Transformar vetor: elevar a potência N
| 06. Contar: Positivos, Negativos e Zeros
| 07. Somatório: De todos, Dos Negativos e dos Positivos
| 08. Exibir Média e Mediana: De Todos, Dos Positivos e Dos Negativos
| 09. Exibir Maior e Menor número
| 10. Sortear dois números: um positivo e um negativo
| 11. Gerar N grupos de T tamanhos. Não repetir valores
| 12. Pedir um novo vetor e verificar se está 100% presente nos números do sistema (e na mesma ordem)
| 13. Top N maiores números
| 14. Top N menores números
| 15. Listar valor médio, e listar números maiores que a Média e Menores que a Média
| 16. Soma da Média dos Números Positivos Múltiplos De dois COM
|   o Produto acumulado dos números negativos pares reduzidos à metade.
| 17. Ordenar os números em ordem crescente:
| 18. Ordenar os números em ordem decrescente
| 19. Eliminar números múltiplos de N e M (simultaneamente)
| 00. Sair
 ==================================================================================================='''
main() 