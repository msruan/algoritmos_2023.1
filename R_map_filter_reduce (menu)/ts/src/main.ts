import {question} from "readline-sync"
import { gerarMenu } from "./utils";

function main () {

    const SAIR = 0;
    const GERAR = 1;
    const MANUAL = 2;
    const AUTO = 3;
    const MOSTRAR = 4;
    const ELEVAR = 5;

    let numeros : number[] = [];
    let opcao = -1;
    let menu : string = gerarMenu("PatroNUMBERS","Gerar vetor, Preencher manual, Preencher auto, "+
    "Mostrar vetor, Elevar a N, Contar positivos, negativos e zeros, Somatório: todos, negativos, positivos, "+
    "Exibir média e mediana: de todos, dos positivos, dos negativos, Exibir maior e menor número, "+
    "Sortear dois números: um positivo e um negativo, Geraar N grupos de T tamanhos(n repetir valores, "+
    "Pedir novo vetotor e verificar se é igual ordenado e/ou desordenado ao atual, "+
    "Top N maiores números, Top N menores números");

    do {
        opcao = parseInt(question(menu));

        if(opcao == GERAR){

            const size = parseInt(question("Deseja gerar um vetor de que tamanho? "));
            let valorPadrao = NaN;
            if(question("Deseja passar um valor padrão? (0 - 1)\n>>> ") == "1")
                valorPadrao = parseInt(question("Digite o valor padrão: "))
            for(let i = 0; i < size; i++)
                numeros.push(valorPadrao);
        }

        else if(opcao == MANUAL){

            for(let i = 0; i < numeros.length; i++)
                numeros[i] = parseInt(question(`Digite o ${i+1}º número: `));
        }

        else if(opcao == AUTO){

        }

        else if(opcao == MOSTRAR){

            console.log(numeros);
        }

        else if(opcao == ELEVAR){

            const fator = parseInt(question("Digite a potência: "));
            numeros.map(function(elemento){
                return Math.pow(elemento,fator);
            });
        }

    }while(opcao != SAIR);
}