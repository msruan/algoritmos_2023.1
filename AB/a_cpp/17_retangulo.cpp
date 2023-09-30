// Leia o valor da base e altura de um retângulo, calcule e escreva sua área. (área = base * altura)
#include <iostream>
using namespace std;

int main(){
    float base, altura, area;
    cout << "============ ÁREA DO RETÂNGULO ===========\n\n";
    cout << "Digite o valor da base.\n>>>";
    cin >> base;
    cout << "\nDigite o valor da altura.\n>>>";
    cin >> altura;
    area = base * altura;
    cout << "\nA área do retângulo é " << area << '.';
}