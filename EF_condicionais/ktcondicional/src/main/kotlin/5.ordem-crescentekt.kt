import kotlin.system.exitProcess

fun main () {
    println("5. Leia 3 (três) números e escreva-os em ordem crescente.\n\n");

    print("Digite o primeiro número: ");
    val first : Int? = readlnOrNull()?.toIntOrNull();
    print("Digite o segundo número: ");
    val second : Int? = readlnOrNull()?.toIntOrNull();
    print("Digite o terceiro número: ");
    val third : Int? = readlnOrNull()?.toIntOrNull();

    if(first == null || second == null || third == null){
        exitProcess(1);
    }

    mostrarOrdemCrescente(first,second,third);
}
fun mostrarOrdemCrescente(a : Int, b : Int, c : Int){

    var maior : Int = -1;
    var meio : Int = -1;
    var menor : Int = -1;
    when {
        c <= a && c <= b -> menor = c;
        a <= b && a <= c -> menor = a;
        b <= a && b <= c -> menor = b;

    }
    when {
        a >= b && a >= c -> maior = a;
        b >= c && b >= a -> maior = b;
        c >= b && c >= a -> maior = c;
    }
    when {
        (a >= c && a <= b ) || (a >= b && a <= c) -> meio = a;
        (b >= c && b <= a ) || (b >= a && b <= c) -> meio = b;
        (c >= b && c <= a ) || (c >= a && c <= b) -> meio = c;
    }

    mostrarNumeros(menor,meio,maior);
}
fun mostrarNumeros(a : Int, b : Int, c : Int){
    println("Em ordem crescente temos: $a, $b, $c.");
}
