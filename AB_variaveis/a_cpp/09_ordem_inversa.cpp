// Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).
#include <iostream>
using namespace std;

int main(){
    float a, b;
    cout << "============== LER A,B MOSTRANDO B,A =============\n\n";
    cout << "Digite o valor de A.\n>>>>";
    cin >> a;
    cout << "\nDIgite o valor de B.\n>>>";
    cin >> b;
    cout << "Você digitou (" << a << ", " << b << "). \nInvertendo, fica (" << b << ", " << a << ").";
}