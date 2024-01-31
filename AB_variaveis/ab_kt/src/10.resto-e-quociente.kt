import kotlin.system.exitProcess
fun main() {

    //Entrada
    println("10. Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.\n");
    print("Digite o primeiro número: ");
    val firstNum : Int? = readlnOrNull()?.toIntOrNull();
    print("Digite o segundo número: ");
    val secondNum : Int? = readlnOrNull()?.toIntOrNull();

    //Processamento
    if(firstNum == null || secondNum == null){
        print("Haha, como você quer usar o programa sem digitar nenhum valor?");
        readlnOrNull();
        exitProcess(1);
    }
    val resto = firstNum % secondNum;
    val quociente = (firstNum / secondNum).toInt();

    //Saída
    println("\n\n***** DIVISAO *****\n")
    println("""
        $firstNum | $secondNum
            ------------
        ($resto)     $quociente
    """.trimIndent());
}