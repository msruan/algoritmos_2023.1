#include <iostream>
using namespace std;
unsigned short input_usi(string label);
void titulo(string texto);
unsigned short duracao(unsigned short inicio_minutos, unsigned short fim_minutos);

void titulo(string texto){
    cout << "============ " << texto << " ============\n\n";
}
unsigned short input_usi(string label){
	unsigned short inteiro;
	cout << label << "\n>>> ";
    cin >> inteiro;
    cout << "\n";
    return inteiro;
}

int main(){
    unsigned short h_inicio, m_inicio, h_fim, m_fim,inicio_minutos,horas_duracao,duracao_em_minutos, fim_minutos,minutos_duracao;
    titulo("DURAÇÃO DO JOGO");
    h_inicio = input_usi("Que horas o jogo começou?");
    m_inicio = input_usi("E quantos minutos?");
    h_fim = input_usi("Que horas terminou?");
    m_fim = input_usi("Quantos minutos?");

    inicio_minutos = (h_inicio * 60 + m_inicio);
    fim_minutos = (h_fim * 60 + m_fim);
    duracao_em_minutos = duracao(inicio_minutos,fim_minutos);
    minutos_duracao = (duracao_em_minutos%60);
    horas_duracao = ((duracao_em_minutos - minutos_duracao) /60);

    cout << "A duração do jogo foi de " << horas_duracao << "h e " << minutos_duracao << "min.\n\n";
}
unsigned short duracao(unsigned short inicio_minutos, unsigned short fim_minutos){
    if (fim_minutos >= inicio_minutos)
        return (fim_minutos-inicio_minutos);
    else
        return (24*60-inicio_minutos+fim_minutos);
}