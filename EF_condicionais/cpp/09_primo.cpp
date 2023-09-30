#include <iostream>
#include <string>
using namespace std;
void titulo(string texto);
int input_i(string label);
bool eh_primo(int numero);
void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}
int input_i(string label){
    int inteiro;
    cout << label << "\n>>> ";
    cin >> inteiro;
    cout << "\n";
    return inteiro;
}
int main(){
    titulo("É PRIMO?");
    int numero = input_i("Digite um inteiro.");
    if (eh_primo(numero))
        cout << "É primo!";
    else
        cout << "Não é primo!";
    cout << "\n\n";
}
bool eh_primo(int numero){
    if (((numero == 2)or(numero==3))or((numero==5)or(numero==7)))
        return true;
    else if(numero ==1)
        return false;
    else if ((((numero % 2) and (numero %3)) and ((numero%5) and (numero%7))))
        return true;
    return false;
}
