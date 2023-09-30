#include <iostream>
using namespace std;
void titulo(string texto);
int main(){
    float real,resto;
    int inteiro;
    titulo("ARREDONDADOR");
    cout << "Digite um número decimal.\n>>> ";
    cin >> real;
    inteiro = real;
    
    if (inteiro > 0){
        resto = real - inteiro;
        if (resto>=0.5)
            inteiro++;
    }
    else{
        resto = -real + inteiro;
        if (resto>=0.5)
            inteiro--;
    }
    cout << "Arredondado: " << inteiro;
}
void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}