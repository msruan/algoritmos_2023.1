// Fórmula da TMB para homens: TMB = 88,36 + (13,4 x peso[kg]) + (4,8 x altura[cm]) - (5,7 x idade)
#include <iostream>
#include <string>
using namespace std;
void titulo(string titul);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}
int main(){
    unsigned short idade, altura, tmb;
    float peso;
    titulo("TMB HOMEM");
    cout << "Digite sua idade.\n>>> ";
    cin >> idade;
    cout << "\nDigite sua altura em CM.\n>>> ";
    cin >> altura;
    cout << "\nDigite o peso em KG.\n>>> ";
    cin >> peso;
    tmb = (88,36 + (13,4 * peso) + (4,8 * altura) - (5,7 * idade));
    cout << "\nTMB: " << tmb <<".\n\n";
}