#Crie um programa que receba a idade de uma pessoa e calcule a sua frequência cardíaca máxima, que é dada pela fórmula 220 menos a idade. O programa deve então calcular a faixa de batimentos cardíacos ideais para atividades físicas moderadas e intensas, que correspondem a 50-70% e 70-85% da frequência cardíaca máxima, respectivamente. Os resultados devem ser exibidos na tela. 

def main() :
    idade = float(input('Quantos anos você tem? '))
    print("Digite 0 para atividade física moderada, e 1 para intensa")
    ativ = int(input('Qual o seu nível de atividade física?(0 ou 1) '))
    freq_max, freq_bat_min, freq_bat_max = calculo(idade, ativ)
    saida(freq_max, freq_bat_max, freq_bat_min)


def calculo(idade,ativ) :       
    freq_max = 220 - idade
    div = freq_max / 100
    freq_bat_min = div * 50 + (div  * (ativ * 20))
    freq_bat_max = div * 70 + (div * (ativ * 15))
    return freq_max, freq_bat_max, freq_bat_min                                      
  
def saida(freq_max, freq_bat_max, freq_bat_min) :
    print('Sua frequência de batimentos cardíacos máxima é de',freq_max,',bpm.')
    print('No seu nível de atividade física, a frequência cardíaca ideal é de',freq_bat_min,'-',freq_bat_max,',bpm.')

main()