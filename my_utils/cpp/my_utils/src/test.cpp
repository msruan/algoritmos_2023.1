#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;
//Mostra os elementos de um vector de strings no formato { | a | b | }
void print(const vector<string>& lista){
    cout << endl <<"[ ";
    for (string i: lista){
        cout << "| "<< i << " ";
    }cout << "| ]"<<endl;
}

vector<string> split(string str){
    vector<string>saida;
    string substr;
    for (char carac: str){
        if (carac != ' '){
            substr.push_back(carac);
        }else if(substr != ""){
            saida.push_back(substr);
            substr = "";
        }
    }if (substr != "")
        saida.push_back(substr);
    return saida;
}
bool contem_substring_separada(string label, string sub,int lenLabel,int lenSub){
    int i,j,controler = 0;
    bool pix = false;
    for (j=0; j < lenSub; j++){
        for (i = controler; i < lenLabel; i++){
            if(label[j] == sub[i]){
                pix = true;
                controler = i+1;
            }
        }
        if(pix)
            pix = false;
        else
            return false;
    }
    return true;
}
bool contem_substring_separada(vector<int> label, vector<int> sub,int lenLabel,int lenSub){
    int i,j;
    static int controler = 0;
    static bool pix = false;
    for (j=0; j < lenSub; j++){
        for (i = controler; i < lenLabel; i++){
            if(sub[j] == label[i]){
                pix = true;
                controler = i+1;
            }
        }
        if(pix)
            pix = false;
        else
            return false;
    }
    return true;
}
int main() {
    /*
    print(split("urubu do pix"));
    bool lindinho = contem_substring_separada(vector<int>{1,2,3,4,5},vector<int>{1,2,4},5,2);
    string saida = lindinho ? "S" : "N";
    cout << saida;
  /*int v, a, b, c; scanf("%d %d %d %d", &v, &a, &b, &c);
  int resp = 0;
  if(v >= a || v >= b || v >= c) resp = 1;
  if(v >= (a + b) || v >= (a + c) || v >= (b + c)) resp = 2;
  if(v >= (a + b + c)) resp = 3;
  printf("%d\n", resp);*/
}
