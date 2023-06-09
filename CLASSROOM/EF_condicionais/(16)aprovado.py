def main():
    prim = float(input('Digite a primeira nota: '))
    seg = float(input('Digite  a segunda nota: '))
    boletim  = prova(prim,seg)
    saida(boletim)

def prova(prim,seg):
    media = (prim + seg) / 2
    if media >= 7:
        boletim = 'aprovado'
    elif media < 7:
        print('O aluno ficou de prova final!')
        final = float(input('Quanto o aluno tirou? '))
        if final >= 7:
            boletim = 'aprovado'
        else:
            boletim = 'reprovado'
    return boletim

def saida(boletim):
    print("O aluno está",boletim,'!')
    
main()