// Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)
#include <iostream>
#include <cmath> // ocpional, para fins de precisão
using namespace std;

int main(){
    float volume, pi, raio;
    pi = M_PI;
    cout << "============ VOLUME DA ESFERA ============\n\n";
    cout << "Digite o valor do raio da esfera. \n>>> ";
    cin >> raio;
    volume = (4 * pi * (raio * raio * raio)) / 3;
    cout << "\nO volume da esfera é " << volume << " u.c.\n\n";
}