//Leia um valor em kg (quilograma), calcule e escreva o equivalente em g (grama).
#include <iostream>
using namespace std;

int main(){
    float kg, mg;
    cout << "============ CONVERSOR KG EM G ============\n\n";
    cout << "Digite o valor em quilogramas.\n>>>";
    cin >> kg;
    mg = kg * 1000;
    cout << '\n' << kg << " kg é igual a " << mg << " gramas.";
}