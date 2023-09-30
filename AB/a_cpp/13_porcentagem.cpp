// 13. Leia um valor em real (R$), calcule e escreva 70% deste valor.
#include <iostream>
using namespace std;

int main(){
    float reais;
    cout << "============= 70% DE UM VALOR EM R$ =============\n\n";
    cout << "Digite o valor em R$;\n>>>";
    cin >> reais;
    reais *= 0.7;
    cout << "70% desse valor corresponde a R$" << reais << ".\n\n";
}