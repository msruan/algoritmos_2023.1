#include <stdio.h>
void somedia(int quantidade);
int main(){
	int quantidade;
	printf("\n******* SOMA E MÉDIA *******\n");
	printf("Quantos números deseja fornecer? \n>>> ");
	scanf("%d",&quantidade);
	printf("\n");
	somedia(quantidade);
}
void somedia(int quantidade){
	float numero, soma = 0, media;

	for (int i = 0; i < quantidade; i++){
		printf("Digite um número:\n>>> ");
		scanf("%g",&numero);
		soma += numero;
	}
	media = (soma/quantidade);
	printf("\nSoma: %g \nMédia: %g \n\n",soma,media);
}