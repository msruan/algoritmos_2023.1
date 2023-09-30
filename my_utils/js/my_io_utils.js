import {question} from 'readline-sync'

function print(...args){
    console.log(...args)
}

function fabrica_print(separador=' '){
    function print(){
        args = Array.from(arguments);  
        for (let i = 0; i < length(args); i++){
            process.stdout.write(args[i],separador);
    }return print;
}
function len(vetor){
    let counter = 0;
    for (let _ of vetor){
        counter++;
    }return counter;
}
function append(vetor,item){
    tamanho = len(vetor);
    vetor[tamanho] = item;
    return vetor;
}

function copy(vetor){
    let lista = [];
    for (let i = 0; i < len(vetor); i++){
        lista = append(vetor,item);
    }return lista;
}

function mapear(vetor,funcao_transformadora){
    lista = copy(vetor)
    for (let item of lista){
        item = funcao_transformadora(item);
    }return lista;
}

function filtrar(vetor,funcao_bool){
    let lista = [];
    for (let item of vetor){
        if (funcao_bool(item)){
            lista = append(item);
        }
    }return lista;
}