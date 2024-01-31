#10. Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.

#entrada
prim = int(input('Insira o primeiro número: '))
seg = int(input('Digite o segundo: '))

#proces
quo = prim // seg
resto = prim % seg

#saída
print('O quociente da divisão do primeiro número pelo segundo é',quo,', e o resto dessa divisão é',resto)