#include <stdio.h>
int main(){
	printf("=========== NUMS ATE N ==========\n\n");
	int numero;
	printf("Digite o valor de n.\n>>> ");
	scanf("%d",&numero);
	for (int i = 1;i < numero;i++)
		printf("%d; ",i);
	return 0;
}