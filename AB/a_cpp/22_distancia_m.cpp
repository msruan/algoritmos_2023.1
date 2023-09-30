// Leia um valor em km, calcule e escreva o equivalente em m.
#include <iostream>
using namespace std;

int main (){
    float kms, metros;
    cout << "============ KMS PARA METROS ===========\n\n";
    cout << "Digite o valor de quilômetros.\n>>> ";
    cin >> kms;
    metros = kms * 1000;
    cout << "\n" << kms << "km é igual a " << metros << " metros.\n\n";
}