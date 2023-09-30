/*Crie um programa que receba a idade de uma pessoa e calcule a sua frequência cardíaca máxima, que é dada pela fórmula 220 menos a idade. 
O programa deve então calcular a faixa de batimentos cardíacos ideais para atividades físicas moderadas e intensas, que correspondem a 50-70% e 70-85% da frequência cardíaca máxima, respectivamente. 
Os resultados devem ser exibidos na tela. */

#include <iostream>
#include <string>
using namespace std;
void titulo(string titul);
int input_i(string label);
unsigned short input_usi(string label);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";}

unsigned short input_usi(string label){
	unsigned short inteiro;
	cout << label << "\n>>> ";
    cin >> inteiro;
    return inteiro;
}

int main(){
	int idade, frequencia;
	float mod_min, mod_max, int_max;
	titulo("CALCULADORA BATIMENTOS");
	idade = input_usi("Digite sua idade.");
	frequencia = 220 - idade;
	mod_min = frequencia * 0.5;
	mod_max = frequencia * 0.7;
	int_max = frequencia * 0.85;	
	cout << "Frequência ideal para atividades moderadas:\n";
	cout << mod_min << " ~ " << mod_max << "bpm\n\n";
	cout << "Frequência ideal para atividades intensas:\n";
	cout << mod_max << " ~ " << int_max << "bpm\n\n";
}
