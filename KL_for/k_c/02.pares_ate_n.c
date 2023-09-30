#include <stdio.h>
int main(){
	printf("=========== PARES ATE N ==========\n\n");
	int numero;
	printf("Digite o valor de n.\n>>> ");
	scanf("%d",&numero);
	for (int i = 1;i < numero;i++){
		if (!(i % 2))
			printf("%d; ",i);
	}
	return 0;
}