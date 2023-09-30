#include <iostream>
using namespace std;
int mdc(int a, int b);
int main(){
    int a,b;
    cout << "==========" << " MDC "<< "==========\n\n";
    cout << "Digite o primeiro número\n>>> ";
    cin >> a;
    cout << "\nDigite o segundo número\n>>> ";
    cin >> b;
    int md_c = mdc(a,b);
    cout <<"\nO mdc de "<<a<<" e "<<b<<" é "<<md_c<<"!\n\n";

}
//v2
int mdc(int a, int b){
    int candidato;
    for (candidato = a; not((a%candidato==0) and (b%candidato==0)) ; candidato--)
        cout<<"";//no additional instructions needed
    return candidato;
}
//v1
/*int mdc(int a, int b){
    int counter = a;
    while (not(((a%counter==0) and (b%counter==0))))
        counter--;
    return counter;
}*/