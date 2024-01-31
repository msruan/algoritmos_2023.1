// Leia o valor da base e altura de um triângulo, calcule e escreva sua área. (área=(base * altura)/2)
#include <iostream>
using namespace std;

int main(){
    float base, altura, area;
    cout << "============ ÁREA DO TRIÂNGULO =============\n\n";

    cout << "Digite o valor da base.\n>>>";
    cin >> base;

    cout << "\nDigite o valor da altura.\n>>>";
    cin >> altura;
    
    area = (base*altura) / 2;
    cout << "\nA área do triângulo é " << area << '.';
}