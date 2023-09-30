//1. Leia N e escreva todos os números inteiros de 1 a N.
import { question } from "readline-sync";
function main(){
    console.log("\n****** NUMS ATE N ******\n")
    const numero = Math.floor(Number(question("Digite um número: ")))
    imprimir_nums_ate_n(numero)
}
function imprimir_nums_ate_n(numero){
    console.log(`\nNúmeros de 1 a ${numero}:`)
    for (let i = 1; i < numero; i++){
        process.stdout.write(`${i}; `)
    }console.log('\n')
}

main()
