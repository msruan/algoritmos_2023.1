#include <stdio.h>
void soma_igual(float numero);
int main(){
	printf("\n****** SOMA IGUAL A N ******\n\n");
	float numero;
	printf("Digite o valor do número: ");
	scanf("%g",&numero);
	soma_igual(numero);
}
void soma_igual(float numero){
	float anterior, atual,contador = 0;
	while (((anterior+atual)!= numero) || (contador<2)){
		anterior = atual;//atribuindo lixo na primeira iteração
		printf("Digite um número: ");
		scanf("%g",&atual);
		contador++;
	}
	printf("\n%g + %g = %g\n",anterior,atual,numero);
}