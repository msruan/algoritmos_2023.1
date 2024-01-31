//
fun main(){

    //Entrada
    println("25. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.\n");
    print("Digite um valor em metros: ");

    //Processamento
    val metrosIn : Int? = readlnOrNull()?.toIntOrNull();

    if(metrosIn == null){
        throw NullPointerException("A entrada foi nula!");
    }
    val kms = (metrosIn - metrosIn % 1000) / 1000;
    val metros = metrosIn % 1000;

    //Saida
    println("\n");
    println("""
        ***** RESULTADOS *****
        
        $metrosIn metros equivale a $kms kms e $metros metros! 
    """.trimIndent());
}