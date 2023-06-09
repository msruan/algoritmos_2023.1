# 1/1 + 3/2 + 5/3 ... 99/50
from funcao import obter_inteiro_maior_que_um,show, mmc, mdc
def main():
    n = obter_inteiro_maior_que_um()
    fracao(n)
def fracao(n):
    numerador_antigo = 1
    denominador_antigo = n
    numerador_atual = 2
    denominador_atual = n - 1
    mm_c= mmc(n,n-1)
    numerador_visual = mm_c / denominador_atual * numerador_atual + mm_c / denominador_antigo * numerador_antigo 
    denominador_visual = mm_c
    show(f'{numerador_antigo} / {denominador_antigo} + ',end='')
    while (denominador_atual - 1) != 0:
        show(f'{numerador_atual} / {denominador_atual} ',end='')
        numerador_atual += 1
        denominador_atual -= 1
        show('+ ',end='')
        mm_c = mmc(denominador_visual,denominador_atual) 
        denominador_visual = mm_c
        numerador_visual = mm_c / denominador_visual * numerador_visual + mm_c / denominador_atual * numerador_atual
    md_c = mdc(numerador_visual,denominador_visual)
    if md_c != 1:
        show (f'= {numerador_visual/md_c} / {denominador_visual/md_c}')
    else:
        show (f'= {numerador_visual/md_c} / {denominador_visual/md_c}')
    '''show(f'+ {n} / 1 ',end='')
    mm_c = denominador_visual
    numerador_visual = mm_c / denominador_visual * numerador_visual + mm_c * n'''
main()