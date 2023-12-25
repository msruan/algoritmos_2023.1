import { question } from "readline-sync";

export function vendaManual(): number[] {

    const bilhete : number[] = new Array(6);

    for(let i = 0; i < 6; i++){
        bilhete[i] = parseInt(question(`Digite o ${i+1}º número: `));
        console.log();
    }
    return bilhete;
}

export function vendaAuto() : number[] {

    const bilhete : number[] = new Array(6);

    for(let i = 0; i < 6; i++){
        bilhete[i] = Math.floor(Math.random() * (60 - 1) + 1); //Math.random() * (max - min) + min;
    }
    return bilhete.sort();
}
