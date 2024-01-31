// Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)
#include <iostream>
using namespace std;

int main(){
    float celsius, fahrens;
    cout << "============ Cº PARA Fº ===========\n\n";
    cout << "Digite a temperatura em Cº.\n>>> ";
    cin >> celsius;
    fahrens = (9 * celsius + 160) / 5;
    cout << "\n" << celsius << "Cº equivale à " << fahrens << "Fº.\n\n";
}