#include <iostream>
#include <string>
#include <cmath>
using namespace std;
void boiada(int quantidade);
int main(){
	int quantidade;
	cout << "===== BOIADA =====\n\n";
	cout << "Quantos bois deseja cadastrar? ";
	cin >> quantidade;
	boiada(quantidade);
}
void boiada(int quantidade){
	int cbf, maior_cbf; //cadastro de boi físico
	float maior_peso = -INFINITY;
	float peso;
	while(quantidade--){

		cout << "\nQual o peso do boi? ";
		cin >> peso;
		cout << "Digite o cbf do boi: ";
		cin >> cbf;

		if (peso > maior_peso){
			maior_cbf = cbf;
			maior_peso = peso;
		}
	}
	cout << "\n**** Maior boi ****\n\n";
	cout << "CBF: " << maior_cbf;
	cout << "\nPeso: " << maior_peso << "\n";		

}