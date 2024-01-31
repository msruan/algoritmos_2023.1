// Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).
#include <iostream>
using namespace std;

int main(){
    float cotacao, dolar, real;
    cout << "=========== DÓLAR PARA REAL =============\n\n";
    cout << "Um dólar equivale a quantos reais?\n>>>";
    cin >> cotacao;
    cout << "\nQuantos dólares você deseja converter?\n>>>";
    cin >> dolar;
    real = dolar * cotacao;
    cout << "\n$" << dolar << " equivale à R$" << real << ".\n\n";
}