#include <iostream>
using namespace std;
int mmc(int a, int b);
int main(){
    int a,b;
    cout << "==========" << " MMC "<< "==========\n\n";
    cout << "Digite o primeiro número\n>>> ";
    cin >> a;
    cout << "\nDigite o segundo número\n>>> ";
    cin >> b;
    int mm_c = mmc(a,b);
    cout <<"\nO mmc de "<<a<<" e "<<b<<" é "<<mm_c<<"!\n\n";

}
//v2
/*
int mmc(int a, int b){
    int candidato;
    for (candidato = a; (not((candidato%a==0) and (candidato%b==0))); candidato++)
        cout<<"";//desnecessário!
    return candidato;
}*/
//v1
int mmc(int a, int b){
    int counter = a;
    while (not(((counter%a==0) and (counter%b==0))))
        counter++;
    return counter;
}
