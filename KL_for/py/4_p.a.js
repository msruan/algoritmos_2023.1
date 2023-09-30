/*const readlineSync = require('readline-sync');*/
import { question } from './utils.js';

function main(){
    const a_zero = Number(question('Digite o primeiro termo da PG: '))
    const razao = Number(question('Digite o quociente da PG: '))
    const limite = Number(question('Qual o limite da PG? '))
    progressao_geometrica(a_zero,razao,limite);
}
function progressao_geometrica(a_zero,quociente,teto){
    show_inline('Termos: ')
    for(let i = a_zero; i < teto; i*=quociente){
        show_inline(`${i}; `)
    }
}
function show_inline(label){
    return process.stdout.write(label)

}
main()