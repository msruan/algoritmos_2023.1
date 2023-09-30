#include <vector>
#include <string>
#include <functional>
#include <iostream>
#include "../../../my_utils/include/io_utils.hpp"
#include "../../../my_utils/include/math_utils.hpp"
#include "../../../my_utils/include/vector_utils.hpp"
#include "../../../my_utils/include/string_utils.hpp"
#include "../../../my_utils/include/all_utils.hpp"
#include <experimental/random>
using namespace std;
using experimental::randint;
//Opcao 1
void gerar_vetor(vector<int>& vetor,int tamanho,int padrao = 0){
    for(int i = 0; i < tamanho; i++)
        vetor.push_back(padrao);
}
void prints(string label){
    cout << label;
}

//Opções 2 e 3
//Retorna um vetor preenchido por um valor padrão
vector<int> preencher_vetor(vector<int> lista, bool manualmente = false){
    if (manualmente){
        for(int i: lista)
            i = inputi("Digite o valor da posição "+str(i+1)+"\n>>> ");
    }else{
        limpar_tela();
        prints("PREENCHENDO O VETOR AUTOMATICAMENTE...\n");
        int min = inputi("Digite o valor mínimo do números: ");
        int max = inputi("Digite o valor máximo dos números: ");
        for (int i: lista){
            i = randint(min,max);
        }
    }
    return lista;
}

//Retorna uma matriz com vetores contendo zeros, positivos e negativos
vector<vector<int>> dividir_vetor(vector<int> lista){
    vector<vector<int>> saida(3,vector<int>(0));
    saida[0] = (mapear([](int i){return i==0;},lista));
    saida[1] = (mapear([](int i){return i>0;},lista));
    saida[2] = mapear([](int i){return i<0;},lista);
    return saida;
}

//Opção 4 e Opção 5(IMPLEMENTADAS)

//Opcao 6
//Mostra quantidade de inteiros positivos, negativos e zeros
void contar_vetor(vector<int>lista){
    vector<vector<int>> divididos = dividir_vetor(lista);
    prints("Zeros: ");
    print(divididos[0]);
    prints("Positivos: ");
    print(divididos[1]);
    prints("Negativos: ");
    print(divididos[2]);
}


//Opção 7
//Mostra os somatórios de todos os números, dos positivos e dos negativos
void mostrar_somatorio(vector<int>lista){
    vector<vector<int>> divididos = dividir_vetor(lista);
    int somatorio_todos = reduzir(lista,somar);
    int somatorio_positivos = reduzir(divididos[1],somar);
    int somatorio_negativos = reduzir(divididos[2],somar);

    prints(gerar_titulo("SOMATÓRIOS"));
    prints("Todes: "+str(somatorio_todos)+"\n");
    prints("Positivos: "+str(somatorio_positivos)+"\n");
    prints("Negativos: "+str(somatorio_negativos)+"\n");
}

//Opção 8
//Mostrar média e mediana de todos, dos positivos e dos negativos
void mostrar_media_e_mediana(vector<int>lista){
    float media_t = reduzir(lista,[](int acumulado,int number){return acumulado+number;})/static_cast<float>(lista.size());
    float media_p = reduzir(filtrar([](int x){return x>0;},lista),[](int acumulado,int number){return acumulado+number;})/static_cast<float>(lista.size());
    float media_n = reduzir(filtrar([](int x){return x<0;},lista),[](int acumulado,int number){return acumulado+number;})/static_cast<float>(lista.size());
    print(gerar_titulo("MEDIA"))
    print("Média de todos: "+str(media_t)+"\n");
    print("Média dos positivos: "+str(media_t)+"\n");
    print("Média de todos: "+str(media_t)+"\n");
    cout << "Números maiores que a média: ";
    print<int>(filtrar([media](int x){return x>media;},lista));
    cout << "Números menores que a média: ";
    print<int>(filtrar([media](int x){return x<media;},lista));
}


//Opção 9
//Exibe maior e menor número
void mostrar_maior_e_menor(vector<int>lista){
    int maior = reduzir(lista,[](int x, int y){return (x>y?x:y);},lista[0]);
    int menor = reduzir(lista,[](int x, int y){return (x<y?x:y);},lista[0]);
    print("\nO maior número é: ",maior,"\nO menor número é: ",menor,'\n');
}

//Opção 10
//Sorteia um número positivo e um número negativo
void sortear(vector<int>lista){
    vector<int> positivos = filtrar([](int x){return x>0;},lista);
    vector<int> negativos = filtrar([](int x){return x<0;},lista);
    if(negativos.size()==0 and positivos.size() == 0)
        return;
    int sorteado;
    if(negativos.size()==0){
        print("O número sorteado é ",positivos[randint(0,(int)positivos.size())]);
    }
    else if(positivos.size()==0){
        print("O número sorteado é ", negativos[randint(0,(int)negativos.size())]);
    }else{
        print("O número positivo sorteado é ",positivos[randint(0,(int)positivos.size())]);
        print("O número sorteado é ", negativos[randint(0,(int)negativos.size())]);
    }
}

//Opção 12
//Compara dois vetores de inteiros


bool comparar_vetores(vector<int> a, vector<int> b){
    if(a.size()!=b.size())
        return false;
    for (int i = 0; i < a.size(); i++){
        if(a[i]!=b[i])
            return false;
    }return true;
}

//Opção 13 e 14
//Retorna uma string com o ranking de números
string mostrar_top_numeros(vector<int>lista,int quantidade, bool maiores=true){
    vector<int> m;
    string saida;
    if(maiores)
        m = quick_sort(lista,true);
    else
        m = quick_sort(lista);
    saida = gerar_titulo("\nTOP " + str(quantidade) + " NÚMEROS\n");
    for(int i = 0; i < quantidade; i++){
        saida += str(i+1)+". "+str(m[i])+"\n";
    }return saida;
}

//Opção 15
//15. Listar valor médio, e listar números maiores que a Média e Menores que a Média
void mostrar_infos_media(vector<int>lista){
    float media = reduzir(lista,[](int x, int y){return x+y;},0)/static_cast<float>(lista.size());
    print("Média: "+str(media)+"\n");
    cout << "Números maiores que a média: ";
    print<int>(filtrar([media](int x){return x>media;},lista));
    cout << "Números menores que a média: ";
    print<int>(filtrar([media](int x){return x<media;},lista));
}

//Opção 18 e Opção 19
void ordenar_condicao(vector<int>&arr,function<bool(int)> funcao_booleana){
    vector<int> filtrados,indices;
    int controle = 0;
    for(int i = 0; i< arr.size(); i++){
        if(funcao_booleana(i)){
            indices.push_back(i);
            filtrados.push_back(arr[i]);
        }
    }
    if(filtrados.size()==0)
        return;
    filtrados = quick_sort(filtrados);//agora ordenados
    for(int i = 0; indices.size() != controle; i++){
        if(indices[controle]==i){
            arr[i] = filtrados[controle];
            controle++;
        }
    }
}

vector<int> ordenar_vetor(vector<int>bagunçado){
    int escolha = obter_opcao(gerar_menu("ORDENAR","Todes, Positivos, Negativos, Pares, Ímpares"),5);
    vector<int> arrumado(0);
    switch (escolha)
    {
    case 1:
        arrumado = quick_sort(bagunçado);
        return arrumado;
    case 2:
        ordenar_condicao(bagunçado,[](int x){return x>0;});
        return bagunçado;
    case 3:
        ordenar_condicao(bagunçado,[](int x){return x<0;});
        return bagunçado;
    case 4:
        ordenar_condicao(bagunçado,[](int x){return x%2==0;});
        return bagunçado;
    case 5:
        ordenar_condicao(bagunçado,[](int x){return x%2==1;});
        return bagunçado;
    default:
        return bagunçado;
    };
    
}
int main(){
    vector<int>pix {-1,3,2,-5,22,43,-4,-2,12};
    print(ordenar_vetor(pix));
}




//Opção 0
