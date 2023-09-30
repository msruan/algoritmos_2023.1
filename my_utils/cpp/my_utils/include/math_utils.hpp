#ifndef MATH_UTILS_H
#define MATH_UTILS_H
#include <functional>
#include <vector>
#include<cmath>
#include <string>
#include "vector_utils.hpp"
using namespace std;
function<int(int)> fabrica_pow(int potencia);
int len_digitos(int numero);
float mediana_vetor(vector<int> lista);
float media_vetor(vector<int> lista);
int somar(int a, int b);
bool eh_par(int a);
bool in(string carac, string label);
#endif
