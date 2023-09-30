#19. Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)

import math
#entrada
raio = float(input("Digite o raio:"))
 
#process
area = (raio ** 3 * 4 * 3.14) / 3

#saida
print('A área da esfera corresponde a',math.floor(area))