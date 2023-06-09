from funcao import show, obter_numero
def main():
    a_zero = obter_numero('Digite o primeiro termo da PA: ')
    razao = obter_numero('Digite a razão da PA: ')
    limite = obter_numero('Quantos termos da PA você quer? ')
    progressao_aritmetica(a_zero,razao,limite)
def progressao_aritmetica(termo,razao,teto):
    count = 0
    while count < teto:
        show(f'{termo}; ',end='')
        termo += razao
        count +=1
main()