#include <iostream>
using namespace std;
#include <string>

void calculadora(float a, float b);
int input_i(string label);

float input_f(string label);
void titulo(string texto);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}

float input_f(string label){
    float real;
    cout << label << "\n>>> ";
    cin >> real;
    cout << "\n";
    return real;
}

int main(){
    float a,b,c, maior;
    titulo("MAIOR DE 3");
    a=input_f("Digite o primeiro número.");
    b=input_f("Digite o segundo número.");
    c=input_f("Digite o terceiro número.");
    maior = a;
    if (b>maior)
        maior = b;
    else if (c>maior)
        maior = c;
    cout << "O maior é" << maior;
}