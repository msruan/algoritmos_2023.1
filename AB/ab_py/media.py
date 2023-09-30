#14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

#entrada
nota1 = float(input('Qual a primeira nota? '))
peso1 = float(input("Qual o peso da primeira nota? "))
nota2 = float(input('Qual a segunda nota? '))
peso2= float(input('Qual o peso da segunda nota? '))
nota3 = float(input('Qual a terceira nota? '))
peso3 = float(input('Qual o peso da terceira nota? '))

#proces
media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

#saída
print('A média ponderada é',media)