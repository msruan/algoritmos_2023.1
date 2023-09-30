def main():
    angulo = float(input('Digite o ângulo: '))
    quadro = verify(angulo)
    saida(quadro)

def verify(angulo):
    if angulo == 0:
        return "seus sonhos! Não existe 0"
    if 0 < angulo <= 90:
        quadro = 1
    if 91 <= angulo <= 180:
        quadro = 2
    if 181 <= angulo <= 270:
        quadro = 3
    if 271 <= angulo <= 3600:
        quadro = 4
    return quadro

def saida(quadro):
    print('O ângulo está no ',quadro,'º quadrante!',sep='')

main()