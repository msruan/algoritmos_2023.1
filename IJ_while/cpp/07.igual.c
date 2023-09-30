#include <stdio.h>
int main(){
	printf("\n******* ACHE O IGUAL *******\n\n");
	float numero,candidato;
	printf("Digite um número e eu irei guardá-lo...\n>>> ");
	scanf("%g",&numero);
	while (1){
		printf("\nDigite um número: ");
		scanf("%g",&candidato);
		if (numero==candidato){
			printf("\nEsse número é igual ao que você digitou!\n");
			return 0;
		}
	}
}