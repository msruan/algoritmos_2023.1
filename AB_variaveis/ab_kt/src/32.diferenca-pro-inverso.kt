import kotlin.system.exitProcess

fun main() {
    print("32. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.\n\n");

    print("Digite um número de três algarismos: ");
    val numero : Int? = readlnOrNull()?.toIntOrNull();
    if(numero == null){
        print("Por favor, tenha certeza de digitar um número!");
        exitProcess(1);
    }

    val centena: Int = (numero - numero % 100)  / 100;
    val dezena : Int = (  (numero % 100) - (numero % 100) % 10 ) / 10;
    val unidade : Int = numero - (centena * 100 + dezena * 10);

    val inverso = unidade * 100 + dezena * 10 + centena;

    print("O inverso de $numero é $inverso!!!\n" +
            "A diferença entre eles é ${numero-inverso}!")
}