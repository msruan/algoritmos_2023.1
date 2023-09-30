#ifndef IO_UTILS_H
#define IO_UTILS_H

#include <iostream>
#include <vector>
#include <string>
#include "vector_utils.hpp"
using namespace std;
void print();
void print(const vector<int>&);
void print(const vector<float>&);
void print(const vector<double>&);
void print(const vector<string>);
template <typename... Args>
void print(const Args&... args);
template <typename tipo>
void print(const vector<tipo>&);
template<typename tipo>
    tipo input(string label="");
int inputi(string label=">>> ");
int obter_opcao(string menu,int numero_de_opcoes);
bool obter_resposta(string pergunta="Sim ou Não?\n>>> ");


#endif
