class Numeros{
	public static String
	public static void main(String args[]){
		Numeros.inverterNumeros(3.f,5.f);
		/*print(Numeros.somarDigitos(10));
		print(Numeros.somarDigitos(19));
		print(Numeros.somarDigitos(999));*/
	}
	public static void print(int numero){
		System.out.println(numero);
	}
	public static void print(float numero){
		System.out.println(numero);
	}
	public static int pow(int base,int expoente){
		int saida = 1;
		for(int i = 1; i <= expoente;i++){
			saida *= base;
		}return saida;
	}
	public static int contarDigitos(int numero){
		int digitos = 1;
		for(int noves = 9; numero>noves; digitos++){
			noves += (9*pow(10,digitos));
		}return digitos;
	}
	public static int calcularQuociente(int a, int b){
		return (a-a%b)/b;
	}
	public static float calcularMedia(int quantidade){
	}
	public static void calcularDivisao(int a, int b){
		System.out.print(a);
		System.out.print("")
	}
	//5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).
	//35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.:número = 9534 ; soma = 9+5+3+4 = 21.
	public static int somarDigitos(int numero){
		int len = Numeros.contarDigitos(numero), somatorio = 0, resto = 0,potencia, digito;
		for(int i = len; i > 0; i--){//199 > 
			potencia = pow(10,i-1);//100
			digito = (numero - numero % potencia)/potencia;
			somatorio += digito;//1
			numero -= (potencia*digito); 
		}return somatorio;
	}
	//7. Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.
	public static void somar_e_subtrair(float a, float b, float c){
		System.out.print("Soma dos primeiros números: ");
		print(a+b);
		System.out.println();
		System.out.print("Diferença entre os últimos: ");
		print(b-c);
	}
	//9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).
	public static void inverterNumeros(float a, float b){
		System.out.print(b);
		System.out.print(", ");
		System.out.print(a);
	}
}
