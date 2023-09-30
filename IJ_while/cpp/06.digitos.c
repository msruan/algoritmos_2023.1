#include <stdio.h>
#include <math.h>
int quantos_digitos(int numero);

int quantos_digitos(int numero){
	numero = ((numero > 0) ? numero : -numero);
	int controle = 9,contador = 1;
	while (numero > controle){
		controle += (round(pow(10,contador)) * 9);
		contador++;
	}
	return contador;
}
int main(){
	printf("\n******* Nº DE DÍGITOS ******\n\n");
	int numero;
	printf("Digite um inteiro: ");
	scanf("%d",&numero);
	int digitos = quantos_digitos(numero);
	printf("\nO número tem %d dígitos!\n",digitos);
}   
