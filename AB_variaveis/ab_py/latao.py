#44. Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.

#entrada
num = float(input('Digite a quantidade inteira de latão em kg: '))

#proces
cobre = num * 700
zinco = num * 300

#saída 
print("cobre:",cobre,'gramas, zinco:',zinco,'gramas')