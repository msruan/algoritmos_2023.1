#obs: as duas progessoes nao funcionam para decrescentes negativas, devido a limitação do menor que limite.
from funcao import number, show, insert
def main():
    a_zero = number(insert('Digite o primeiro termo da PG: '))
    razao = number(insert('Digite o quociente da PG: '))
    limite = number(insert('Qual o limite da PG? '))
    progressao_geometrica(a_zero,razao,limite)
def progressao_geometrica(a_zero,quociente,teto):
    termo = a_zero 
    for i in range(a_zero,teto):
        
    while termo < teto:
        show(f'{termo}; ',end='')
        termo *= quociente
main()