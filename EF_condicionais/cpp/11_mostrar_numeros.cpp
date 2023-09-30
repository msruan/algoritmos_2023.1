#include <iostream>
#include <string>
using namespace std;
float input_f(string label);
void titulo(string texto);
void menu(float a, float b, float c);
void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}
float input_f(string label){
    float real;
    cout << label << "\n>>> ";
    cin >> real;
    cout << "\n";
    return real;
}
int main(){
    titulo("MOSTRAR NÚMERO");
    float a = input_f("Digite o primeiro número");
    float b = input_f("Digite o segundo número");
    float c = input_f("Digite o terceiro número");
    menu(a,b,c);
}
void menu(float a, float b, float c){
    cout << "Digite qual número deseja mostrar:\n(1,2,3)\n>>> ";
    unsigned short opcao;
    cin >> opcao;
    cout <<"\n";
    switch(opcao){
    case 1:
        cout << "Mostrando o 1º número...\n"<<a;
        break;
    case 2:
        cout << "Mostrando o 2º número...\n"<<b;
        break;
    case 3:
        cout << "Mostrando o 3º número...\n"<<c;
        break;
    }
    cout<<"\n";
}