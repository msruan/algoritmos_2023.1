from funcao import show, obter_inteiro_maior_que_um
def main():
    numero = obter_inteiro_maior_que_um('Quer quantos números? ')
    fibbonaci(numero)

def fibbonaci(numero):
    anterior = 0
    atual = 1
    count = 1
    show ('0; 1; ',end='')
    while count <= numero: 
        soma = atual + anterior
        show(f'{soma}; ',end='')
        anterior = atual
        atual = soma
        count += 1
main()