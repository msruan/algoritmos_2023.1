// Leia o valor do lado de um quadrado, calcule e escreva sua área. (área = lado²)
#include <iostream>
using namespace std;

int main(){
    float lado, area;
    cout << "============= ÁREA DO QUADRADO ============\n\n";
    cout << "Digite o valor do lado do quadrado.\n>>>";
    cin >> lado;
    area = lado * lado;
    cout << "\nA área do quadrado de lado " << lado << " é " << area << '.';
}