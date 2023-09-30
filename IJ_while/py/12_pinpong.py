from funcao import insert, show, obter_inteiro_positivo
from funcao import mostrar_divisao as linha

def main():
    show('Programa em execução!')
    nome_a = insert('Qual o nome do jogador A?')
    nome_b = insert('Qual o nome do jogador B?')
    quant_pontos = obter_inteiro_positivo('De quantos pontos a partida será? ')
    quant_margem = obter_inteiro_positivo('Qual deve ser a diferença de pontos entre eles? ')
    poing(nome_a,nome_b,quant_pontos,quant_margem)

def poing(a,b,quant_pontos,quant_margem):
    pontos_a = 0
    pontos_b = 0
    while not ha_ganhador(pontos_a,pontos_b,quant_pontos,quant_margem):
        ponto = insert('Quem fez ponto? (A-B)')
        if ponto.upper()=='A':
            pontos_a += 1
        elif ponto.upper()=='B':
            pontos_b += 1
        else:
            continue
    vencedor = quem_ganhou(pontos_a,pontos_b)
    resultado(vencedor, a, b, pontos_a, pontos_b)

def ha_ganhador(a,b,pontos,margem):
    return ((a-b >=margem or b-a>=margem) and (a>=pontos or b>=pontos))
def quem_ganhou(a,b):
    if a > b:
        return 'a'
    else:
        return 'b'

def resultado(ganhou, a, b, p_a, p_b):
    linha('='*30)
    if ganhou == 'a':
        show(f'Parabéns ao jogador {a} pela vitória!')
    else:
        show(f'Parabéns ao jogador {b} pela vitória com diferença de {abs(p_a-p_b)} pontos!')
    linha('='*15 + 'Placar' + 15*'=')
    show(f'O jogador {a} fez {p_a} pontos.')
    show(f'O jogador {b} fez {p_b} pontos.')

main()