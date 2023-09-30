#include <iostream>
#include <functional>
using std::cout;
template <typename... Args>
void print(const Args&... args){//,char end='\n',char sep=" "){
        //cout << ' ' << ... << args;
    for(const auto& i: {args...})
        cout <<  ' ' <<i;
}


int main(){
    print("urubu do pis");
}