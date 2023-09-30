#include <iostream>
using namespace std;
int produto(int a, int b);
int main(){
    int a,b;
    cout << "==========" << " PRODUTO "<< "==========\n\n";
    cout << "Digite o primeiro número\n>>> ";
    cin >> a;
    cout << "\nDigite o segundo número\n>>> ";
    cin >> b;
    int multiplicacao = produto(a,b);
    if (a>=b)
        cout<<"  "<<a<<"\n *"<<b<<"\n------\n  "<<multiplicacao;
    else
        cout<<"  "<<b<<"\n *"<<a<<"\n------\n  "<<multiplicacao;
    //cout <<"\nO produto de "<<a<<" e "<<b<<" é "<<multiplicacao<<"!\n\n";
}
int produto(int a,int b){
    int produto_final=0;
    bool sinais_diferentes= (((a>=0)and(b>=0))or((a<=0)and(b<=0))) ? false : true;
    //para negativos
    if (a<0)
        a=-a;
    if (b<0)
        b=-b;
    for(int i = b;i>0;i--)
        produto_final+=a;
    if (sinais_diferentes)
        return (-produto_final);
    return (produto_final);
}