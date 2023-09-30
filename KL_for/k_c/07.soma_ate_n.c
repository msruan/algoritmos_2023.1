#include <stdio.h>
int main(){
	printf("\n********* SOMA ATE N *********\n\n");
	int numero;
	int soma = 0;
	printf("Digite o valor de n.\n>>> ");
	scanf("%d",&numero);
	for (int i = 1; i <= numero; i++)
		soma += i;
	printf("Soma: %d\n\n",soma);
}