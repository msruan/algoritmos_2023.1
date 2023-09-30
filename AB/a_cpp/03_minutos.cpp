//Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.
#include <iostream>
using namespace std;

int main(){
    int horas, minutos, resultado;
    cout << "============ CONVERSOR HORAS E MINUTOS EM MINUTOS =============\n\n";
    cout << "Quantas horas?\n>>>";
    cin >> horas;
    cout << "Quantos minutos?\n>>>";
    cin >> minutos;
    resultado = (horas * 60 + minutos);
    cout << "\nIsso corresponde à " << resultado << " minutos.";
}
