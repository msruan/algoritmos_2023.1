#include <iostream>
using namespace std;
#include <string>

int input_i(string label);

short input_si(string label);

unsigned short input_usi(string label);
float input_f(string label);
void titulo(string texto);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}
float input_f(string label){
    float real;
    cout << label << "\n>>> ";
    cin >> real;
    cout << "\n";
    return real;
}
unsigned short input_usi(string label){
	unsigned short inteiro;
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

int input_i(string label){
    int inteiro;
    cout << label << "\n>>> ";
    cin >> inteiro;
    cout << "\n";
    return inteiro;
}


