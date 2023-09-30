#include <iostream>
using namespace std;
#include <string>

unsigned short quantos_iguais(float a,float b,float c);
float inputf(string label);
void titulo(string texto);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}

float inputf(string label){
    float real;
    cout << label << "\n>>> ";
    cin >> real;
    cout << "\n";
    return real;
}
int main(){
    titulo("ORDEM CRESCENTE");
    float a = inputf("Digite o primeiro número");
    float b = inputf("Digite o segundo número");
    float c = inputf("Digite o terceiro número");
    unsigned short iguais = quantos_iguais(a,b,c);
    float menor = a;
    float maior = a;
    float meio = a;
    if (iguais==0){
        if (b>maior)
            maior = b;
        if (c>maior)
            maior = c;
        if(b<menor)
            menor = b;
        if(c<menor)
            menor = c;
        if ((b<maior) and (b>menor))
            meio = b;
        if ((c< maior) and (c>menor))
            meio = c;
    }
    else if(iguais == 2){
        if (a==b){
            if (a<c)
                maior = c;
            else
                menor = c;
        } else if(a==c){
            if (a<b)
                maior = b;
            else
                menor = b;       
        } else if (b==c){
            if (a<c){
                maior = c;
                meio = c;
            } else{
                menor = c;
                meio = c;
            }
        }
    }
    cout << "Em ordem crescente temos:\n" <<menor<<", "<<meio<<", "<<maior<<"\n\n";
}
unsigned short quantos_iguais(float a,float b,float c){
    unsigned short iguais = 1;
    if (a==b)
        iguais++;
    if (a==c)
        iguais++;
    if (b==c)
        iguais++;
        //
    if (iguais == 1)
        iguais = 0;
    else if (iguais ==4)
        iguais = 3;
    return iguais;
}