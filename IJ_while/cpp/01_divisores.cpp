#include <iostream>
#include <string>
using namespace std;
int input(string label);
unsigned short inputp(string label);
bool eh_divisor(int candidato,int numero);
int input(string label){
    int num;
    cout << label << "\n>>> ";
    cin >> num;
    return num;
}
unsigned short inputp(string label){
    short num;
    cout << label << "\n>>> ";
    cin >> num;
    return num;
}
void titulo(string texto){
    cout << "============= " << texto << " =============\n\n";
}
int main(){
    int numero;
    titulo("DIVISORES");
    unsigned short quantidade = inputp("Quantos números você irá fornecer?");
    if (not quantidade){
        cout << "\nVocê está brincando?";
        return main();
    }
    do{//bastava um for
        numero = input("\nDigite o valor do número:"); 
        cout << "\nDivisores:\n";
        if (numero > 0){
            for (int i = numero;i;i--){
                if (eh_divisor(i,numero))
                    cout << i<< "; ";
            }
        } else{
            for (int i = numero;i;i++){
                if (eh_divisor(i,numero))
                    cout << i<< "; ";
            }    
        }
    cout <<"\n";
    } while(--quantidade);
    cout <<"\n\n";
}
bool eh_divisor(int candidato,int numero){
    return(not(numero%candidato));
}