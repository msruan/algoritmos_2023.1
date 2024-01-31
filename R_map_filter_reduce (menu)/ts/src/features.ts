import {question} from "readline-sync"
import { randint } from "./utils";

export function elevarNumsVetor(fator : number, numeros : number[]){

    numeros.map(function(elemento){
        return Math.pow(elemento,fator);
    });
}

export function preencherAuto(numeros: number[], min : number, max : number){

    for(let i = 0; i < numeros.length; i++)
        numeros[i] = randint(min,max);
}

export function preencherManual(numeros : number[]){

    for(let i = 0; i < numeros.length; i++)
        numeros[i] = parseInt(question(`Digite o ${i+1}º número: `));
}

export function preencherValorPadrao(numeros : number[] ,size: number, valorPadrao: number) {
    for (let i = 0; i < size; i++)
        numeros.push(valorPadrao);
}

function ehNegativo(numero){return numero < 0;}
function ehZero(numero){return numero == 0;}

function getNegativos(numeros : number[]){

    const ehNegativo = (numero : number) => numero < 0;
    return numeros.filter(ehNegativo);
}

function getPositivos(numeros : number[]){
    const ehPositivo = (numero: number) => numero > 0;
    return numeros.filter(ehPositivo);
}

function getZeros(numeros : number[]){
    const ehZero = (numero : number) => numero == 0;
    return numeros.filter(ehZero);
}

export function contagemPositivos(numeros : number[]) : number{

    const positivos = getPositivos(numeros);
    return positivos.length;
}

export function contagemNegativos(numeros : number[]) : number{

    const negativos = getNegativos(numeros);
    return contagemNegativos.length;
}

export function contagemZeros(numeros : number[]) : number{

    const zeros = getZeros(numeros);
    return zeros.length;
}


export function somatorio(numeros : number[]) : number{

    const funSoma = (acumulado, atual) => acumulado + atual;
    const soma = numeros.reduce(funSoma, 0);
    return soma;
}

export function somatorioPositivos(numeros : number[]) : number{

    const positivos = getPositivos(numeros);
    return somatorio(positivos);
}

export function somatorioNegativos(numeros : number[]) : number{

    const positivos = getNegativos(numeros);
    return somatorio(positivos);
}

export function calcularMaior(numeros : number[]) : number{

    let maior : number = NaN;

    const funCalcularMaior = (acumulado : number, atual : number) => atual > acumulado ? atual : acumulado;
   
    if(numeros.length > 0){
        maior = numeros.reduce( funCalcularMaior, Number.NEGATIVE_INFINITY);
    }
    return maior;
}

export function calcularMenor(numeros : number[]) : number{

    let menor : number = NaN;

    const funCalcularMenor =  (acumulado : number, atual : number) => atual < acumulado ? atual : acumulado;
   
    if(numeros.length > 0){
        menor = numeros.reduce( funCalcularMenor, Number.POSITIVE_INFINITY);
    }
    return menor;
}


export function mediana(numeros : number []) : number{

    const ordenados = numeros.sort();
    const ehPar = (numero) => numero % 2 == 0;
    const size = numeros.length;
    let mediana : number;

    if(ehPar(size))
        mediana = ( numeros[(size/2)-1] + numeros[size/2] ) / 2;
    else
        mediana = numeros[(size-1)/2];
    return mediana;
}

export function medianaPositivos(numeros : number[]){

    const positivos = getPositivos(numeros);
    return mediana(positivos);
}

export function medianaNegativos(numeros : number[]){

    const negativos = getNegativos(numeros);
    return mediana(negativos);
}

export function media(numeros : number []) : number{

    return somatorio(numeros) / numeros.length;
}

export function mediaPositivos(numeros : number []){

    return media(getPositivos(numeros));
}

export function mediaNegtivos(numeros : number[]) : number{

    return media(getNegativos(numeros));
}

export function sortearPositivo(numeros : number[]) : number{


}