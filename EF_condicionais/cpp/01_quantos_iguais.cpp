#include <iostream>
#include <string>
using namespace std;
void titulo(string texto);
float inputf(string label);
unsigned short quantos_iguais(float a,float b,float c);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}

float inputf(string label){
    float real;
    cout << label << "\n>>> ";
    cin >> real;
    cout << "\n";
    return real;
}
int main(){
    float a,b,c;
    unsigned short iguais = 1;
    titulo("IGUAIS");
    a = inputf("Digite o primeiro número");
    b = inputf("Digite o segundo número");
    c = inputf("Digite o terceiro número");
    iguais = quantos_iguais(a,b,c);
    if (iguais)
        cout << "\nHá "<<iguais<< " números iguais!\n\n";
    else
        cout <<"Não há números iguais!";
}
unsigned short quantos_iguais(float a,float b,float c){
    unsigned short iguais = 1;
    if (a==b)
        iguais++;
    if (a==c)
        iguais++;
    if (b==c)
        iguais++;
        //
    if (iguais == 1)
        iguais = 0;
    else if (iguais ==4)
        iguais = 3;
    return iguais;
    }