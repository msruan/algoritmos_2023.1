#include "../include/io_utils.hpp"
//Função print genérica
template <typename... Args>
void print(const Args&... args,end='\n',sep=" "){
        //cout << ' ' << ... << args;
    for(const auto& i: {args...})
        cout << sep << args;
    cout << end;
}

//Printa uma linha vazia
void print(){
    cout << '\n';
}

    //Mostra os elementos de um vector de inteiros no formato { | 1 | 2 | }
void print(const vector<int> lista){
    cout << endl <<"[ ";
    for (int i: lista){
        cout << "| "<< i << " ";
    }cout << "| ]"<<endl;
}
//Mostra os elementos de um vector de inteiros no formato { | 1 | 2 | }
void print(const vector<float>& lista){
    cout << endl <<"[ ";
    for (int i: lista){
        cout << "| "<< i << " ";
    }cout << "| ]"<<endl;
}

//Mostra os elementos de um vector de inteiros no formato { | 1 | 2 | }
void print(const vector<double>& lista){
    cout << endl <<"[ ";
    for (double i: lista){
        cout << "| "<< i << " ";
    }cout << "| ]"<<endl;
}

//Mostra os elementos de um vector de strings no formato { | a | b | }
void print(const vector<string>& lista){
    cout << endl <<"[ ";
    for (string i: lista){
        cout << "| "<< i << " ";
    }cout << "| ]"<<endl;
}

//Mostra os elementos de um vector de strings no formato { | a | b | }
template<typename tipo>
void print(const vector<tipo> lista){
    cout << endl <<"[ ";
    for (tipo i: lista){
        cout << "| "<< i << " ";
    }cout << "| ]"<<endl;
}

template<typename tipo>
tipo input(const string label=""){
    print(label);
    tipo saida;
    cin >> saida;
}

int inputi(string label=">>> "){
    cout << label;
    int numero;
    cin >> numero;
    return numero;
}

int inputu(string label=">>> "){
    int numero;
    do{
        cout << label;
        cin >> numero;
    }while(numero < 0);
    return numero;
}

string inputs(string label=">>> "){
    cout << label;
    string saida;
    cin >> saida;
    return saida;
}

int obter_opcao(string menu,int numero_de_opcoes){
    int numero;
    do{
        numero = inputi(menu);
        limpar_tela();
    }while(numero_de_opcoes < numero < 0 );
        return numero;
}

bool obter_resposta(string pergunta="Sim ou Não?\n>>> "){
    string opcao = inputs(pergunta);
    if (in(opcao,"Ss1TtYy") or ta_em(opcao,{"SIM","sim","Sim"}))
        return true;
    else if(in(opcao,"Nn0Ff") or ta_em(opcao,{"NAO","nao","Nao","Não","NÃO","não"}))
        return false;
    return obter_resposta(pergunta);
}

