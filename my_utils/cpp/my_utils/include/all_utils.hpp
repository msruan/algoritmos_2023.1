#ifndef ALL_UTILS_H
#define ALL_UTILS_H
#include <iostream>
#include <vector>
#include <experimental/random>
#include <string>
#include "string_utils.hpp"
#include "io_utils.hpp"
using namespace std;
using experimental::randint;
//Diversas
void limpar_tela();
void enter_limpar_tela(string label);
void trocar_variaveis(int& a,int& b);
//Retorna um título no formato:
//\******** TITULO *********
string gerar_titulo(string titulo);
//Gera um menu com o título e as opções recebidas
string gerar_menu(string titulo,string opcoes);
void tchau();
#endif
