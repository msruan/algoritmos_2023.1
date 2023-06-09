from funcao import show, obter_numero
def main():
    a_zero = obter_numero('Digite o primeiro termo da PG: ')
    quociente = obter_numero('Digite o quociente da PG: ')
    limite = obter_numero('Quantos termos da PG você quer? ')
    progressao_geometrica(a_zero,quociente,limite)
def progressao_geometrica(termo,quociente,teto):
    count = 0
    while count < teto:
        termo *= quociente
        show(f'{termo}; ',end='')
        count +=1