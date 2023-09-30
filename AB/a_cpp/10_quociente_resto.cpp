// Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.
#include <iostream>
using namespace std;

int main(){
    int a, b, quociente, resto;
    cout << "============ QUOCIENTE E RESTO ============\n\n";
    cout << "Digite o primeiro número.\n>>>";
    cin >> a;
    cout << "\nDigite o segundo número.\n>>>";
    cin >> b;
    resto = a % b;
    quociente = (a-resto) / b;
}