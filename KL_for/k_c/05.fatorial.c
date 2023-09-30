#include <stdio.h>
int main(){
	printf("\n============ FATORIAL =========\n\n");	
	int numero;
	int fatorial = 1;
	printf("Digite o valor de n.\n>>> ");
	scanf("%d",&numero);
	printf("\nFatorial: ");

	if (numero){
		for(int i = 1; i <= numero; i++)
			fatorial *= i; 
	}else{
		printf("1\n\n");
		return 0;
	}

	printf("%d \n\n",fatorial);
}