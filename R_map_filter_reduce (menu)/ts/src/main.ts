import {question} from "readline-sync"
import * as utils from "./utils";
import * as feats from "./features";

function main () {

    const SAIR = 0;
    const GERAR = 1;
    const MANUAL = 2;
    const AUTO = 3;
    const MOSTRAR = 4;
    const ELEVAR = 5;
    const CONTAGEM = 6;
    const SOMATORIO = 7;
    const MEDIA = 8;
    const LIMITES = 9;


    let numeros : number[] = [];
    let menu : string = utils.gerarMenu("PatroNUMBERS","Gerar vetor, Preencher manual, Preencher auto, "+
        "Mostrar vetor, Elevar a N, Contar positivos, negativos e zeros, Somatório: todos, negativos, positivos, "+
        "Exibir média e mediana: de todos, dos positivos, dos negativos, Exibir maior e menor número, "+
        "Sortear dois números: um positivo e um negativo, Gerar N grupos de T tamanhos(n repetir valores, "+
        "Pedir novo vetotor e verificar se é igual ordenado e/ou desordenado ao atual, "+
        "Top N maiores números, Top N menores números");

    let opcao = -1;


    while(opcao != SAIR){

        opcao = parseInt(question(menu));


            if(opcao == GERAR){//1

                const size : number = parseInt(question("Deseja gerar um vetor de que tamanho? "));
                let valorPadrao = NaN;
            
                if(utils.lerSimOuNao())
                    valorPadrao = parseInt(question("Digite o valor padrão: "))

                feats.preencherValorPadrao(numeros, size, valorPadrao);
            }
                
            
            else if(opcao == MANUAL)//2

                feats.preencherManual(numeros);
                

            else if(opcao == AUTO){//3

                const min : number = parseInt(question("Digite um valor mínimo: "));
                const max : number = parseInt(question("Digite o valor máximo: "));
                feats.preencherAuto(numeros, min, max);
            }

                
            else if(opcao == MOSTRAR)//4
                console.log(numeros);
                

            else if(opcao == ELEVAR){//5

                const fator = parseInt(question("Digite a potência: "));
                feats.elevarNumsVetor(fator, numeros);
            }

            else if(opcao == CONTAGEM){//6

                const submenu = utils.gerarMenu("CONTAGEM","Positivos, Negativos, Todos, Zeros ");
                const escolha = parseInt(submenu);
                menuSecundarioContagem(numeros, escolha);
            }
                

            else if(opcao == SOMATORIO){//7

                const submenu = utils.gerarMenu("SOMATORIO","Positivos, Negativos, Todos ");
                const escolha = parseInt(submenu);
                menuSecundarioSoma(numeros, escolha);
            }


            else if(opcao == MEDIA){//8
                
                const submenu = utils.gerarMenu("MÉDIA & MEDIANA","Positivos, Negativos, Todos ");
                const escolha = parseInt(submenu);
                menuSecundarioMedia(numeros, escolha);
            }
                

            else if(opcao == LIMITES){//9

                const menor : number = feats.calcularMenor(numeros);
                const maior : number = feats.calcularMaior(numeros);  

                console.log("Menor número: ",menor);
                console.log("Maior número: ",maior);
            }
                
        
            else
                console.log("Opção inválida!");
    }
    utils.bye();
}



function menuSecundarioMedia(numeros : number[], escolha: number){

    const POSITIVOS = 1;
    const NEGATIVOS = 2;
    const TODOS = 3;

    switch(escolha){

        case TODOS:

            console.log("A média de todos os números é: ",feats.media(numeros));
            console.log("A mediana de todos os números é: ",feats.mediana(numeros)); 
            break;

        case POSITIVOS:

            console.log("A média dos números positivos é: ",feats.mediaPositivos(numeros));
            console.log("A mediana dos positivos é: ",feats.medianaPositivos(numeros)); 
            break;

        case NEGATIVOS:

            console.log("A média dos números negativos é: ",feats.mediaNegtivos(numeros));
            console.log("A mediana dos negativos é: ",feats.medianaNegativos(numeros)); 
            break; 
    }
}


function menuSecundarioSoma(numeros : number[], escolha : number){

    const POSITIVOS = 1;
    const NEGATIVOS = 2;
    const TODOS = 3;

    switch(escolha){

        case TODOS:

            console.log("A soma de todos os números é: ",feats.somatorio(numeros));
            break;

        case POSITIVOS:

            console.log("A soma dos números positivos é: ",feats.somatorioPositivos(numeros));
            break;

        case NEGATIVOS:

            console.log("A soma dos negativos é: ",feats.somatorioNegativos(numeros));
            break;
    }
}

function menuSecundarioContagem(numeros : number[], escolha : number){

    const POSITIVOS = 1;
    const NEGATIVOS = 2;
    const ZEROS = 3;

    switch(escolha){

        case POSITIVOS:

            console.log("O total de positivos é: ",feats.contagemPositivos(numeros));
            break;

        case NEGATIVOS:

            console.log("O total de negativos é: ",feats.contagemNegativos(numeros));
            break;

        case ZEROS:

            console.log("O total de zeros é: ",feats.contagemZeros(numeros));
            break;
    }
}
function main2 (){

    const readlineSync = require('readline-sync');

    function exibirMenu(opcoes) {
        console.log('Escolha uma opção:');
        opcoes.forEach((opcao, index) => {
            console.log(`${index + 1}. ${opcao}`);
        });

        const escolha = readlineSync.keyIn('Digite o número da opção e pressione Enter: ', { limit: '$<1-' + opcoes.length + '>' });
        return parseInt(escolha) - 1;
    }

    const opcoesMenu = ['Opção 1', 'Opção 2', 'Opção 3', 'Sair'];

    let escolha;
    do {
        escolha = exibirMenu(opcoesMenu);

        switch (escolha) {
            case 0:
                console.log('Você escolheu a Opção 1');
                break;
            case 1:
                console.log('Você escolheu a Opção 2');
                break;
            case 2:
                console.log('Você escolheu a Opção 3');
                break;
            case 3:
                console.log('Saindo do programa. Até logo!');
                break;
            default:
                console.log('Opção inválida. Tente novamente.');
        }
    } while (escolha !== 3);
    
}
main2();