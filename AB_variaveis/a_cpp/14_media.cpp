//Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.
#include <iostream>
using namespace std;

int main(){
    float nota1, nota2, nota3, peso1, peso2, peso3, media;
    cout << "============= MÉDIA PONDERADA DAS NOTAS ===========\n\n";

    cout << "Digite o primeiro peso.\n>>>";
    cin >> peso1;
    cout << "Digite a primeira nota.\n>>>";
    cin >> nota1;

    cout << "\nDigite o segundo peso.\n>>>";
    cin >> peso2;
    cout << "Digite a segunda nota.\n>>>";
    cin >> nota2;

    cout << "\nDigite o terceiro peso.\n>>>";
    cin >> peso3;
    cout << "Digite a terceira nota.\n>>>";
    cin >> nota3;

    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3);
    cout << "A média é igual a " << media << '.'; 
}