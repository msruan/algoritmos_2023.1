def main() :
    num = int(input('Digite um número entre 0 e 100: '))
    primo = verify(num)
    saida(primo)
def verify(num):
    if num == 0 or num == 1 or num == 2 or num == 3 or num == 5 or num == 7:
        primo = True
    elif num > 0 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0):
        primo = False
    elif num > 0 and (num % 2 != 0 or num % 3 != 0 or num % 5 != 0 or num % 7 != 0) :
        primo = True
    return primo
def saida(primo):
    if primo == True:
        print('O número é primo!')
    else:
        print('O número não é primo!')
main()