// Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.
#include <iostream>
#include <string> // opcional
using namespace std;

int main(){
    float salario, novo_salario;
    string moeda;
    cout << "=============== AUMENTO DE 25% ===============\n\n";

    cout << "Digite o valor do salário.\n>>>";
    cin >> salario;

    cout << "\nDigite a moeda.\n>>>";
    cin >> moeda;
    
    novo_salario = salario * 1.25;
    cout << "\nCom um aumento de 25%, o novo salário é " << moeda << novo_salario << '.';
}