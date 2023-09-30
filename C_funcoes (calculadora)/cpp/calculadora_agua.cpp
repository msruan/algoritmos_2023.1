/*Crie um programa que receba o peso e a atividade física diária de uma pessoa e calcule a quantidade de água que ela deve beber por dia. 
A quantidade de água recomendada é de 35 ml por quilo de peso para pessoas com atividade física moderada, e 45 ml por quilo de peso para pessoas com atividade física intensa. 
O resultado do cálculo deve ser exibido na tela. 
*/
#include <iostream>
using namespace std;
#include <string>
void titulo(string titul);
void titulo(string titul){
    cout << "============ " << titul << " ============\n\n";
}



int main(){
    float peso, agua;
    int ativ_fisica;
    titulo("CALCULADORA ÁGUA");
    cout << "Digite seu peso.\n>>> ";
    cin >> peso;
    cout << "Digite seu nível de atividade física.\n(0)- Moderada; (1) - Intensa\n>>> ";
    cin >> ativ_fisica;
    ativ_fisica = (ativ_fisica * 10) + 35;
    agua = ativ_fisica * peso;
    cout << "Você deve beber " << agua << "ml de água para se manter saudável!";
}


