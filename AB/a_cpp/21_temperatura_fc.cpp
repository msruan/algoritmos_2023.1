// Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).
#include <iostream>
using namespace std;
int main(){
    float celsius, fahrens;
    cout << "============ Fº PARA Cº ===========\n\n";
    cout << "Digite a temperatura em Fº.\n>>> ";
    cin >> fahrens;
    celsius = (5 * fahrens - 160) / 9;
    cout << "\n" << fahrens << "Fº equivale à " << celsius << "Cº.\n\n";
}