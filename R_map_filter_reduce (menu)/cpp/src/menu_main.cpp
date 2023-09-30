/*
8. Exibir Média e Mediana: De Todos, Dos Positivos e Dos Negativos

11. Gerar N grupos de T tamanhos. Não repetir valores


17. Somatório da Média dos Números Positivos múltiplos de dois COM o Produto acumulado dos números negativos pares reduzidos à metade

18. Ordenar os números em ordem crescente: 
Pergunta se: todos, ou apenas pares, ou impares, ou positivos ou negativos, ou ainda apenas os múltiplos (positivos ou negativos) de N

19. Ordenar em ordem decrescente
Pergunta se: todos, ou apenas pares, ou impares, ou positivos ou negativos, ou ainda apenas os múltiplos (positivos ou negativos) de N

0. Sair (mensagem automática de tchau)
*/
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <experimental/random>
#include <functional>
#include "../../../my_utils/include/io_utils.hpp"
using namespace std;
using experimental::randint;

int main(){
    string menu; 
    bool ha_vetor = false;
    vector<int> lista(0);
    int opcao;
    do{
        if (not ha_vetor){
            menu = gerar_menu("MENU","Gerar novo vetor"); 
            opcao = obter_opcao(menu,1);
        }
        switch (opcao)
        {
        case 1:
            /*1. Gerar vetor N posições, pedir valor padrão
            Pedi N ao usuário e gera um vetor com todas as posições vazia (None ou undefined) ou com valor padrão se fornecido
            python: vetor = [None] * N
            javascript: vetor = Arrays(N)
            Em seguida, use sua função mapear para preencher com o valor padrão, ou seja, transformar cada item no valor que o usuário pediu*/
            int tamanho = inputi("Qual o tamanho do vetor?\n>>> "), padrao = 0;
            if(obter_resposta("Deseja fornecer um valor padrão?\n>>> "))
                padrao = inputi("Digite o valor padrão desejado: ");
            gerar_vetor(lista,tamanho,padrao);
            ha_vetor = true;
            break;
        case 2:
            /*2. Preencher vetor manualmente item a item
            Pedi ao usuário sequencialmente cada dos valores (somente números)*/
            lista = preencher_vetor(lista,true);    
            break;
        case 3:
            /*3. Preencher vetor automaticamente
            Peça ao usuário valores Mínimos e Máximos*/
            lista = preencher_vetor(lista);
            break;
        case 4:
            /*4. Mostrar vetor
            Mostra os elementos do vetor*/
            print<int>(lista);
            break;
        case 5:
            /*5. Transformar vetor: elevar a potência N
            Substitui cada item por seu quadrado se expoente for 2, por exemplo*/
            int potencia = input<int>("Deseja elevar à qual potência?");
            lista = mapear(fabrica_pow(potencia),lista);
            break;
        case 6:
            /*6. Contar: Positivos, Negativos e Zeros*/
            contar_vetor(lista);--
            break;
        case 7:
            /*7. Somatório: De todos, Dos Negativos e dos Positivos
            Exibir as 3 informações sobre os valores*/
            mostrar_somatorio(lista);
            break;
        case 9:
            /*9. Exibir Maior e Menor número*/
            mostrar_maior_e_menor(lista);
            break;
        case 10:
            sortear(lista);
            break;
        /*case 12:
            /*12. Pedir um novo vetor e verificar se está 100% presente nos números do sistema (e na mesma ordem)*/
            /*vector<int> teste = input<vector<int>>("Digite o vetor: ");
            comparar_vetores(lista,teste);*/
        case 13:
            //13. Top N maiores números
            int quantidade = input<int>("Quantos números deseja mostrar no ranking? ");
            print(mostrar_top_numeros(quantidade),true);
            break;
        case 14:
            //14. Top N menores números
            int quantidade = input<int>("Quantos números deseja mostrar no ranking? ");
            print(mostrar_top_numeros(quantidade));
            break;
        case 15:
            break;
        case 20:
            int m = input<int>("Digite o valor de m: ");
            int n = input<int>("Digite o valor de n: ");
            lista = filtrar([m,n](int x){return x%(m*n)==0;},lista);
        default:
            break;
        }
        //else if(opcao == 8)
            //mostrar_media_mediana(lista);
    }while(opcao);
}
