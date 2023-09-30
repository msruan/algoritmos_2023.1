#include "../include/all_utils.hpp"
//Diversas
void limpar_tela(){
    system("clear||cls");
}
void enter_limpar_tela(string label=""){
    input<string>(label);
    system("clear||cls");
}

void trocar_variaveis(int& a,int& b){
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
}

//Retorna um título no formato:
//\******** TITULO *********
string gerar_titulo(string titulo){
    return "\n******** "+titulo+" ********\n";
}

//Gera um menu com o título e as opções recebidas
string gerar_menu(string titulo,string opcoes){
    string menu = gerar_titulo(titulo);
    vector<string> opc = split(opcoes,", ");
    for(int i = 1; i <= opc.size(); i++){
        menu += ("| " + (i > 9 ? str(i) : ("0"+str(i))) + " - " + opc[i-1] + "\n");
    }return (menu += "| 00 - Sair\n");
}

//Printa uma despedida aleatória
void tchau(){
    vector<string> substantivo {"minha paçoca","meu pastel de queijo","minha salada de frutas","meu sonho de valsa","meu ouro branco","meu pudim"};
    vector<string> interjeicao {"Adeus","Até logo","Nos vemos em breve","Te vejo em breve","Até mais","Bye","Tchau","Adiós","Goodbye","Sayonara"};
    int s_index = randint(0,static_cast<int>(interjeicao.size()));
    int i_index = randint(0,static_cast<int>(interjeicao.size()));
    cout << "\n"+interjeicao[i_index]+substantivo[s_index]+'!';
}