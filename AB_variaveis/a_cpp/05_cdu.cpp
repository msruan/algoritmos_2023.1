//Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).
#include <iostream>
using namespace std;

int main(){
    int numero, centena, dezena, unidade, soma;
    cout << "============= SOMA DOS ALGARISMOS ============\n\n";
    cout << "Digite um inteiro de 3 dígitos.\n>>>";
    cin >> numero;
    centena = numero / 100;
    dezena = numero % 100;
    unidade = dezena % 10;
    dezena /= 10;
    soma = centena + dezena + unidade;
    cout << "\nA soma dos algarismos é igual a " << soma << ".\n\n";
}