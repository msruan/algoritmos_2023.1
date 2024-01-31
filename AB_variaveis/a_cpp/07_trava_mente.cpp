// Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.
#include <iostream>
using namespace std;

int main(){
    float a, b, c, soma_ab, diff_bc;
    cout << "============ TRAVA MENTE ===========\n\n";
    cout << "Digite o primeiro número.\n>>>";
    cin >> a;
    cout << "\nDigite o segundo número.\n>>>";
    cin >> b;
    cout << "\nDigite o terceiro número.\n>>>";
    cin >> c;
    soma_ab = a+b;
    diff_bc = b-c;
    cout << "\nA soma dos 2 primeiros números é " << soma_ab << '.';
    cout << "\nA diferença entre os 2 últimos números é " << diff_bc << ".\n\n";
}