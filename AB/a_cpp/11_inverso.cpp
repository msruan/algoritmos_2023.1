//Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)
#include <iostream>
using namespace std;

int main(){
    int numero, inverso, centena, dezena, unidade;
    cout << "============= MOSTRADOR DE INVERSO ===========\n\n";
    cout << "Digite um inteiro de 3 algarismos.\n>>>";
    cin >> numero;
    centena = numero / 100; //aqui estou me confiando que ele só vai pegar a parte inteira
    dezena = (numero / 10);
    dezena %= 10;
    unidade = (numero % 100) % 10;
    inverso = unidade * 100 + dezena * 10 + centena;
    cout << "\nO inverso de " << numero << " é " << inverso << '.';
}
