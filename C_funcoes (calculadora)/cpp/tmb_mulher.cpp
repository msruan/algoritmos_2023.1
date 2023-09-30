// Fórmula da TMB para mulheres: TMB = 447,6 + (9,2 x peso) + (3,1 x altura) - (4,3 x idade)
#include <iostream>
#include <string>
using namespace std;
void titulo(string titul);
int input_i(string label);
unsigned short input_usi(string label);
short input_si(string label);
float input_f(string label);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}
int input_i(string label){
    int inteiro;
    cout << label << "\n>>> ";
    cin >> inteiro;
    cout << "\n";
    return inteiro;
}
short input_si(string label){
	short inteiro;
    cout << label << "\n>>> ";
    cin >> inteiro;
    cout << "\n";
    return inteiro;
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
    unsigned short idade, altura, tmb;
    titulo("TMB MULHER");
    idade = input_usi("Digite sua idade.");
    altura = input_usi("Digite sua altura em CM.");
    float peso = input_f("Digite o peso em KG.");
    tmb = (447,6 + (9,2 * peso) + (3,1 * altura) - (4,3 * idade));
    cout << "\nTMB: " << tmb <<".\n\n";
}