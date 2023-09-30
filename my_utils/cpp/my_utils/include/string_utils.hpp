#ifndef STRING_UTILS_H
#define STRING_UTILS_H
#include <string>
#include "math_utils.hpp"
#include <cmath>
#include <vector>
using namespace std; 
//*std::String
//Lê um dígito do tipo inteiro e o retorna com std::string
std::string int2str(int digito);
//Preenche uma std::string com *
std::string preencher(int chars);
//Recebe um inteiro e o retorna como std::string
std::string str(int inteiro);
//Retorna um vetor com os índices da primeira posição das substrings encontradas
std::vector<int> buscar_substring(std::string label,std::string substr);
//Parte uma std::string com base no separador fornecido
//!OBS: Não funciona com caracteres multibyte
std::vector<std::string> split(std::string label,std::string separador=", ");
//Parte uma std::string com base no char fornecido
std::vector<std::string> split(std::string label,char separador=' ');
#endif