#include "../include/math_utils.hpp"
//*Math
function<int(int)> fabrica_pow(int potencia){
    auto my_pow = [potencia](auto base) {
        return static_cast<int>(std::pow(base, potencia));};
    return my_pow;
}
int len_digitos(int numero){
	numero = ((numero > 0) ? numero : -numero);
	int controle = 9,contador = 1;
	while (numero > controle){
		controle += (round(pow(10,contador)) * 9);
		contador++;
	}
	return contador;
}
float mediana_vetor(vector<int> lista){
    float mediana;
    vector<int> lista_ordenada = quick_sort(lista);
    if(eh_par(lista.size()))
        mediana = (lista_ordenada[(lista.size()/2)-1]+lista_ordenada[lista.size()/2]) / 2;
    else
        mediana = lista_ordenada[((lista.size()+1)/2)-1];
    return mediana;
}

float media_vetor(vector<int> lista){
    int soma = reduzir(lista,somar);
    return soma / lista.size();
}
int somar(int a, int b){return a+b;}
bool eh_par(int a){return a%2==0;}

bool in(string carac, string label){
    if(carac.size() > 1)
        return false;
    for(char letra : label){
        if (label[0] == letra)
            return true;
    }return false;
}
