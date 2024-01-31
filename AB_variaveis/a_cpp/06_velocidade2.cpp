// Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)
#include <iostream>
using namespace std;

int main(){
    float kmh_velocidade, ms_velocidade;
    cout << "============= KM/H PARA M/S =============\n\n";
    cout << "Digite a velocidade em km/h.\n>>>";
    cin >> kmh_velocidade;
    ms_velocidade = kmh_velocidade / 3.6;
    cout << "\nA velocidade convertida ficou " << ms_velocidade << "m/s.";
}