// Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.
#include <iostream>
using namespace std;

int main(){
    float a,b,soma,diff,div;
    cout << "============ TRAVA MENTE-MENTE ===========\n\n";
    cout << "Digite o primeiro número.\n>>>";
    cin >> a;
    cout << "\nDigite o segundo número.\n>>>";
    cin >> b;
    soma = a+b;
    diff = a-b;
    div = soma / diff;
    cout << "\nA divisão de " << soma << " por " << diff << " é igual a " << div << ".\n\n";
}
