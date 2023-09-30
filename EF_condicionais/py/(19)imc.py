def main():
    altura = float(input('Digite a sua altura em metros: '))
    peso = float(input('Digite seu peso: '))
    imc = calculo_imc(altura,peso)
    saida(imc)
def calculo_imc(altura,peso):
    imc = peso / (altura ** 2)
    return imc
def saida(imc):
    print('Seu IMC é de',imc,'.')
    if imc < 25:
        print("Seu IMC está normal!")
    if 30 >= imc >= 25:
        print('Seu IMC indica que você está obeso!')
    if imc > 30:
        print("Seu IMC indica obesidade mórbida!")

main()