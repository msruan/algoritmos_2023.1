# 1/1 + 3/2 + 5/3 ... 99/50
from funcao import obter_inteiro_maior_que_um,show, mmc
def main():
    n = obter_inteiro_maior_que_um()
    fracao(n)
def fracao(n):
    numerador_atual = 3
    denominador_atual = 2
    denominador_visual = 2
    numerador_visual = 5
    show('1 / 1 + ',end='')
    while denominador_atual <= n:
        show(f'{numerador_atual} / {denominador_atual} ',end='')
        denominador_atual += 1
        numerador_atual += 2
        if denominador_atual > n:
            break
        show('+ ',end='')
        mm_c = mmc(denominador_visual,denominador_atual) 
        numerador_visual = mm_c / denominador_visual * numerador_visual + mm_c / denominador_atual * numerador_atual 
        denominador_visual = mm_c
    show (f'= {numerador_visual} / {denominador_visual}')
main()