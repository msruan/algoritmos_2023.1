#include <iostream>
#include <string>
using namespace std;
bool eh_par(int numero);
bool eh_impar(int numero);
void titulo(string texto);
int input_i(string label);
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
    titulo("PAR ÍMPAR");
    int numero = input_i("Digite um inteiro.");
    if (eh_par(numero))
        cout << "É par!";
    if (eh_impar(numero))
        cout << "É ímpar!";
    cout << "\n\n";
}
bool eh_par(int numero){
    return (!(numero % 2));
}
bool eh_impar(int numero){
    return (numero % 2);
}