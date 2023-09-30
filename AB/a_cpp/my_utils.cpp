#include <iostream>
#include <string>
using namespace std;

//prototipes
int quociente(int a, int b);
void titulo(string label);
int obter_inteiro(string label);
float obter_float(string label);
void show(string label);

int obter_inteiro(string label){
    int numero;
    cout << label << "\n>>>";
    cin >> numero;
    return (numero);
}
float obter_float(string label){
    float numero;
    cout << label << "\n>>>";
    cin >> numero;
    return (numero);
}
void show(string label){
    cout << label << "\n";
}
void titulo(string label){
    cout << "============ " << label << " ============\n\n";
}
int quociente(int a, int b){
    int resto = a%b;
    int quociente = (a-resto) / b;
    return quociente;
}