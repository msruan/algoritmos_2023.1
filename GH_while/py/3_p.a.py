from funcao import number, show, insert
def main():
    a_zero = number(insert('Digite o primeiro termo da PA: '))
    razao = number(insert('Digite a razão da PA: '))
    limite = number(insert('Qual o limite da PA? '))
    progressao_aritmetica(a_zero,razao,limite)
def progressao_aritmetica(a_zero,razao,teto):
    termo = a_zero
    while termo < teto:
        show(f'{termo}; ',end='')
        termo += razao
main()