//1. Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
#include <iostream>
using namespace std;
int main(){
    float ms_velocidade;
    cout << "========== CONVERSOR M/S EM KM/H ==========\n";
    cout << "\nDigite uma velocidade em m/s!\n>>>";
    cin >> ms_velocidade;
    float km_velocidade = ms_velocidade * 3.6;
    cout << "\nA velocidade " << ms_velocidade << "m/s é igual a "  << km_velocidade << "k/h.";
}