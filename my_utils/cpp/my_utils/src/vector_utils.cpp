#include "../include/vector_utils.hpp"
//*std::Vector
vector<int> mapear(function<int(int)> funcao_transformadora,vector<int>lista){
    for (int i: lista)
        i = funcao_transformadora(i);
    return lista;
}
vector<int> filtrar(function<bool(int)> funcao_booleana,vector<int>lista){
    vector<int> saida(0);
    for (int i: lista){
        if(funcao_booleana(i))
            saida.push_back(i);
    }
    return lista;
}
vector<int> filtrar(vector<int>lista,function<int(bool)> funcao_booleana){
    vector<int> saida(0);
    for (int i: lista){
        if(funcao_booleana(i))
            saida.push_back(i);
    }
    return lista;
}
vector<int> filtrar(vector<int>lista,function<bool(int)> funcao_booleana){
    vector<int> saida(0);
    for (int i: lista){
        if(funcao_booleana(i))
            saida.push_back(i);
    }
    return lista;
}

vector<int> filtrar(function<int(bool)> funcao_booleana,vector<int>lista){
    vector<int> saida(0);
    for (int i: lista){
        if(funcao_booleana(i))
            saida.push_back(i);
    }
    return lista;
}

int reduzir(vector<int>lista, function<int(int,int)>operacao_redutora,int acumulado = 0){
    for(int i: lista){
        acumulado = operacao_redutora(acumulado,i);
    }return acumulado;
}

//Verifica a presença de um inteiro em um std::vector
bool ta_em (int numero ,std::vector<int> numeros){
    for(int i: numeros){
        if(numero == i)
            return true;
    }return false;
}

//Verifica a presença de uma std::string em um std::vector
bool ta_em (std::string label ,std::vector<std::string> labels){
    for(std::string i: labels){
        if(label == i)
            return true;
    }return false;
}

vector<int> bubble_sort(vector<int> lista,bool reverse=false){
    bool houve_trocas = false;
    auto comparacao = reverse ? [](int a,int b){return a<b;} : [](int a,int b){return a>b;};

    for(int i = 0; i < lista.size()-1; i++){
        houve_trocas = false;
        for(int j = 0; j < lista.size()-1; j++){
            if(comparacao(lista[j], lista[j+1])){
                trocar_variaveis(lista[j],lista[j+1]);
                houve_trocas = true;
            }
        }if(not houve_trocas)
            break;
    }return lista;
}

vector<int> concatenar_vetores(const vector<int>& a,const vector<int>& b, const vector<int>& c){
    vector<int>saida(0);
    for(int i: a)
        saida.push_back(i);
    for(int i: b)
        saida.push_back(i);
    for(int i: c)
        saida.push_back(i);
    return saida;
}

vector<int> quick_sort(vector<int> lista, bool reverse=false){
    if(lista.size() < 2)
        return lista;
    int pivo = lista[randint<int>(0,lista.size()-1)];
    vector<int> maiores, menores, iguais;
    for (int i: lista){
        if (i > pivo)
            maiores.push_back(i);
        else if(i < pivo)
            menores.push_back(i);
        else    
            iguais.push_back(i);
    }
    vector<int> maiores_ordenados = quick_sort(maiores);
    vector<int> menores_ordenados = quick_sort(menores);
    if (reverse)
        return concatenar_vetores(maiores_ordenados,iguais,menores_ordenados);
    return concatenar_vetores(menores_ordenados,iguais,maiores_ordenados);
}
