#ifndef VECTOR_UTILS_H
#define VECTOR_UTILS_H
#include <vector>
#include <string>
#include <functional>
#include "all_utils.hpp"
#include <experimental/random>
using namespace std;
using experimental::randint;
//*std::Vector
vector<int> mapear(function<int(int)> funcao_transformadora,vector<int>lista);
vector<int> filtrar(function<bool(int)> funcao_booleana,vector<int>lista);
int reduzir(vector<int>lista, function<int(int,int)>operacao_redutora,int acumulado = 0);
bool ta_em (int numero ,std::vector<int> numeros);
bool ta_em (string label ,std::vector<string> labels);
vector<int> bubble_sort(vector<int> lista,bool reverse=false);
vector<int> concatenar_vetores(const vector<int>& a,const vector<int>& b, const vector<int>& c);
vector<int> quick_sort(vector<int> lista, bool reverse=false);
#endif 
