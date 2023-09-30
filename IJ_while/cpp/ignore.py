vetor = [1,2,3]
aux = vetor[:]
for i in range(len(vetor)):
	aux[i] = vetor[-(i+1)]
	print(aux)
print(aux)
"""
print(vetor)
i = 0
while True:
	if len(vetor)%2:
		if i == len(vetor)//2+1:
			break
	if len()
		vetor[i], vetor[i-1] = vetor[i-1], vetor[i]
		print(vetor)
	i +=1
print(f'final: {vetor}')
"""