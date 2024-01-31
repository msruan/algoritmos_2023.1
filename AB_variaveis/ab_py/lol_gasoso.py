#40. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

#entrada
anos = int(input('Há quantos anos você fuma? '))
cigarros = int(input('Quantos cigarros por dia? '))
maço = int(input('Quanto custa o maço? '))

#proces
custo = (anos * 365 * cigarros) / 20
preço = custo * maço

#saída
print('O custo é de',preço,'reais!')
print('Pense duas vezes antes de fumar.')