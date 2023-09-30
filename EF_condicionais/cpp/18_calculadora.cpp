#include <iostream>
using namespace std;
#include <string>

void calculadora(float a, float b);

float input_f(string label);
unsigned short input_usi(string label);
void titulo(string texto);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}
unsigned short input_usi(string label){
	unsigned short inteiro;
	cout << label << "\n>>> ";
    cin >> inteiro;
    cout << "\n";
    return inteiro;
}

float input_f(string label){
    float real;
    cout << label << "\n>>> ";
    cin >> real;
    cout << "\n";
    return real;
}

int main(){
    float a,b;
    titulo("CALCULADORA");
    a = input_f("Digite o primeiro número.");
    b = input_f("Digite o segundo número.");
    calculadora(a,b);
}

void calculadora(float a, float b){
    float soma, diff, produto, div;
    switch (input_usi("Digite a operação que deseja.\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")){
    case 1:
        soma = a+b;
        cout << "A soma entre "<<a<<" e "<<b<<" é "<<soma;
        break;
    case 2:
        diff = a-b;
        cout <<"A diferença entre "<<a<<" e "<<b<<" é "<<diff;
        break;
    case 3:
        produto = a*b;
        cout <<"O produto entre "<<a<<" e "<<b<<" é "<<produto;
        break;
    case 4:
        div = a/b;
        cout <<"A divisão entre "<<a<<" e "<<b<<" é "<<div;
        break;
    }
}