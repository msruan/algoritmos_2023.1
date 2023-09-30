//Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.
#include <iostream>
using namespace std;

int main(){
    int horas, minutos;
    float resultado;
    cout << "============ CONVERSOR HORAS E MINUTOS EM HORAS =============\n\n";
    cout << "Quantas horas?\n>>>";
    cin >> horas;
    cout << "Quantos minutos?\n>>>";
    cin >> minutos;
    resultado = (horas * 60 + minutos) / 60.;
    cout << "\nIsso corresponde à " << resultado << " horas.";
}
