//import java.util.Scanner;
public class Numero{
    
    public static void main(String args[]){
    }
    //1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
    public static int contarIguais(double a, double b, double c){
        return (a==b ? 
            (b==c ? 3 : 2)
            :(b==c ? 2 : 0));
    }
    //2. Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.
    public static void mostrarMaiorEMenor(double a, double b){
        if(a==b)
            System.out.println("Os dois números são iguais!");
        System.out.print(a>b?a:b);
        System.out.println(" é o maior número!");
        System.out.print(a<b?a:b);
        System.out.println(" é o menor número!");
    }
    //3. Leia 3 (três) números, verifique e escreva o menor e o maior entre os números lidos.
    public static void mostrarMaiorEMenor(double a, double b,double c){
        int iguais = contarIguais(a, b, c);
        if(iguais == 3)
            System.out.println("Os três números são iguais!");    
        else{
            System.out.print((a>b ? (a>c?a:c) : (b>c?b:c) ));
            System.out.println(" é o maior número!");
            System.out.print((a<b ? (a<c?a:c) : (b<c?b:c) ));
            System.out.println(" é o menor número!");
        }
    }
    //4.Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade.
    public static boolean algarismosSaoIguais(int num){
        return (num / 10 == num % 10 ? true : false);
    }

    //5. Leia 3 (três) números e escreva-os em ordem crescente.
    public static void mostrarOrdemCrescente(double a, double b, double c){
        int iguais = contarIguais(a, b, c);
        if(iguais == 3){
            System.out.printf("Em ordem crescente temos %f, %f e %f",a,b,c);
        }else{
            double maior = (a>b? (a>c?a:c): (b>c?b:c));
            double menor = (a<b? (a<c?a:c): (b<c?b:c));
            double meio = (a!=maior && a!=menor ? a: (b!= maior && b!= menor ? b : c));
            System.out.printf("Em ordem crescente temos %.1f, %.1f e %.1f",menor,meio,maior);
        }
    }
    /*7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
    (três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
    formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
    escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero). */
    public static boolean ehTriangulo(double a, double b, double c){
        return (a+b>c ? (b+c>a ? (a+c > b ? true: false): false): false);
    }
    public static String tiparTriangulo(double a, double b, double c){
        if(!ehTriangulo(a, b, c))
            return "undefined";
        if(a==b){
            if(b==c)
                return "equilatero";
            return "isosceles";
        }else if(b == c)
            return "isosceles";
        return "escaleno";
    }
    //9. Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.
    public static boolean ehPrimo(int num){
        return(num == 1? false :(num == 3 || num == 5 || num == 7 || num == 2) ||
        (num % 2 != 0 && num % 3 != 0 && num % 5 != 0 && num % 7 != 0 && num % 11 != 0));
    }

    /*11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
    valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
    possíveis para a variável opção são 1, 2 e 3. */
    public static void mostrarOpcao(int opcao, double num1, double num2, double num3){
        System.out.printf("O número escolhido foi %f",(opcao == 1 ? num1 : (opcao == 2 ? 2 : 3)));
    }

    //12. Leia um número e escreva se é par ou ímpar
    public static boolean ehPar(int number){
        return number % 2 == 0;
    }//12. Leia 1 (um) número inteiro e escreva se este número é par ou impar
    public static boolean ehImpar(int number){
        return number % 2==1;
    }

    /*15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
    Escreva na tela qual dos professores tem salário total maior. */
    public static void mostrarMaiorSalario(int horas1, double salario1, int horas2, double salario2){
        System.out.printf("O maior salário é do %do professor!",(horas1*salario1 > horas2*salario2 ? 1 : 2));
    }

    //21. Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso contrario, é arredondado para o inteiro imediatamente inferior.
    public static double arredondar(double numero){
        double fracionario = numero % 1;
        if(fracionario >= 0.5)
            return 1-fracionario+numero;
        return numero-fracionario;
    }

    
}