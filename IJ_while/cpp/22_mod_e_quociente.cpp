#include <iostream>
using namespace std;
void divisao(int a, int b);
int main(){
    int a,b;
    cout << "==========" << " QUOCIENTE E RESTO "<< "==========\n\n";
    cout << "Digite o primeiro número\n>>> ";
    cin >> a;
    cout << "\nDigite o segundo número\n>>> ";
    cin >> b;
    divisao(a,b);
    //cout <<"\nO produto de "<<a<<" e "<<b<<" é "<<multiplicacao<<"!\n\n";
}
void divisao(int a,int b){
    if (b==0){
        cout<<"Não há divisão por 0!";
        return;
    } 
    int quociente = 0;
    int resto = 0;
    if (a<b){
        resto = a;
    } else{
        int x = a;
    while(x>0){
        if(x-b>=0)
            quociente++;
        else
            resto = x;
        x-=b;
        } 
    }
    
    //cout <<"\nQuociente: "<<quociente<< "\nResto: " <<resto<<"\n ";
    cout <<"\n "<< a << "   |_"<<b<<"__\n("<<resto<<")    "<<quociente;
    return;
}
