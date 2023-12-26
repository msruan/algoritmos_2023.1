import {question} from 'readline-sync';
import { gerarMenu, limparConsole } from './utils';
import * as feats from './features';

function main(){

    const SAIR = 0;
    const AUTO = 1;
    const MANUAL = 2;
    const ARRECADADO = 3;
    const SORTEIO = 4;
    const VENCEDORES = 5;
    const ZERAR = 6;

    const PRECO = parseFloat(question("Digite o preço do bilhete: "));

    let menu: string;
    let escolha: number = -1;

    const bilhetes : number[][] = [];
    let vencedores : number[][] = [];
    let numsPremiados : number[] = [];

    do{
        console.log(bilhetes.length)
        menu = gerarMenu("PatroBET", (numsPremiados.length < 1 ? "VENDA AUTO, VENDA MANUAL, " : "##########, ############, ") 
            + (bilhetes.length > 0 ? "MOSTRAR ARRECADADO, " : "##################, ") + 
            (numsPremiados.length < 6 && bilhetes.length > 0 ? "REALIZAR SORTEIO, " : "################, ")+
                (vencedores.length > 0 ? "MOSTRAR VENCEDORES," : "##################, ") + (bilhetes.length > 0 ? " ZERAR" : "#####"));
        
        escolha = parseInt(question(menu));

        if(escolha == AUTO)
            bilhetes.push(feats.vendaAuto());
        
        
        else if(escolha == MANUAL)
            bilhetes.push(feats.vendaManual());
        

        else if(escolha == ARRECADADO)
            console.log("O arrecadado total é ",bilhetes.length * PRECO);

        else if(escolha == SORTEIO){

            numsPremiados = feats.vendaAuto();
        }

        else if(escolha == VENCEDORES){

            // if(vencedores.length == 0){
            //     let acertos = 0;
            //     vencedores = bilhetes.filter(
            //         function(elemento){
            //             acertos = 0;
            //             elemento.forEach(function(numero){
            //                 if(numsPremiados.includes(numero))
            //                     acertos++;
            //             });
            //         }
            //     );
            // }
            // console.log(vencedores);

        }

        limparConsole();
    }while(escolha != SAIR);
}
main();