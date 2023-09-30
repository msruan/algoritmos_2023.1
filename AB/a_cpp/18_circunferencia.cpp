// Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)
#include <iostream>
#include <cmath>
using namespace std;

int main(){
    float raio, comprimento;
    float pi = M_PI;
    cout << "============ COMPRIMENTO DA CIRCUNFERÊNCIA ============\n\n";
    cout << "Digite o valor do raio.\n>>> ";
    cin >> raio;
    comprimento = 2 * pi * raio;
    cout << "\nO comprimento da circunferência é " << comprimento << "u.c.\n\n";
}