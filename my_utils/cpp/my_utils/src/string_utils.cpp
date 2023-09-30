#include "../include/string_utils.hpp"
//*std::String
//Lê um dígito do tipo inteiro e o retorna com std::string
std::string int2str(int digito)
{   
    if (digito ==1)
        return "1";
    else if (digito ==2)
        return "2";
    else if (digito ==3)
        return "3";
    else if (digito ==4)
        return "4";
    else if (digito ==5)
        return "5";
    else if (digito ==6)
        return "6";
    else if (digito ==7)
        return "7";
    else if (digito ==8)
        return "8";
    else if (digito ==9)
        return "9";
    else if (digito ==0)
        return "0";
    return "";
}
//Preenche uma std::string com *
std::string preencher(int chars){
    std::string saida;
    for(int i = 0; i < chars; i++)
        saida += "*";
    return saida;
}
//Recebe um inteiro e o retorna como std::string
std::string str(int inteiro){
    int len = len_digitos(inteiro), i = 1;//73
    std::string saida = "";

    do{
        int auxiliar = std::pow(10,len-i);
        saida += int2str(inteiro / auxiliar);
        inteiro %= auxiliar; 
        i++;
    }while(i < len+1);

    return saida;
}

//Retorna um vetor com os índices da primeira posição das substrings encontradas
std::vector<int> buscar_substring(std::string label,std::string substr){
    std::vector<int>indices(0);
    std::string substring = "";
    for (int i = 0; i+substr.size() <= label.length(); i+=substr.size()){        
        for(int j = i;j<i+substr.size();j++){
            substring += label[j];
        }if(substr ==substring)
            indices.push_back(i);
        substring = "";
    }return indices;
}
//Parte uma std::string com base no separador fornecido
//!OBS: Não funciona com caracteres multibyte
std::vector<std::string> split(std::string label,std::string separador=", ")
{
    std::vector <std::string> saida(0);
    std::string substring = "";
    std::vector<int> indices = buscar_substring(label,separador);
    for (int i = 0; i < label.size();){
        if (not ta_em(i,indices)){
            substring.push_back(label[i]);
            i++;
        }
        else {
            if(substring != ""){
                saida.push_back(substring);
                substring = "";            
            }
            i+=separador.size();
        }
    }if(substring != "")
        saida.push_back(substring);
    return saida;
}
//Parte uma std::string com base no char fornecido
std::vector<std::string> split(std::string label,char separador=' ')
{
    std::vector <std::string> saida(0);
    std::string substring = "";
    for (int i = 0; i < label.size(); i++){
        if (label[i] != separador){
            substring.push_back(label[i]);
        }
        else if(substring != ""){
            saida.push_back(substring);
            substring = "";
        }
    }if(substring != "")
        saida.push_back(substring);
    return saida;
}
