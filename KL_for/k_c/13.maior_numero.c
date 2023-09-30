#include <stdio.h>
#include <float.h>
void maior_numero(int quantidade);

int main(){
	printf("\n========= O MAIOR ========\n\n");
	int quantidade;
	printf("Quantos números deseja ler?\n>>> ");
	scanf("%d",&quantidade);
	maior_numero(quantidade);
}

void maior_numero(int quantidade){
	float numero, maior = FLT_MIN; //menor valor que um float pode assumir
	
	for (int i = 0; i < quantidade; i++){
		printf("Digite um número.\n>>> ");
		scanf("%f",&numero);
		maior = (numero > maior ? numero : maior);
	}
	printf("\nMaior número:%f\n",maior);

}