const readlineSync = require('readline-sync');
export function insert(label=''){
    return readlineSync.question(label)
}
export function obter_numero(label='Digite um número: '){
    const num = insert(label)
    if (eh_numero(num)){
        return toNumber(num)}
    return obter_numero('Por favor, insira um número válido: ')
}
/*1.INPUT/OUTPUT*/
export function mostrar_texto(label=''){ 
    return console.log(label)
}

export function mostrar_texto_inline(label=''){
    return process.stdout.write(label)
}

export function mostrar_texto_caixa_alta(string=''){
    mostrar_texto(mapear(para_maiusculo,string))
}

export function mostrar_texto_caixa_baixa(string=''){
    mapear(para_minusculo,string)
}

export function obter_texto(label='Digite um texto: '){
    texto = readlineSync.question(label)
    if (texto == ''){
        return obter_texto(label)
    }
    return texto
}

export function obter_texto_tam_minimo(tamanho_minimo,label=''){/*label = aquela mensagemzinha que a gente manda pro input*/
    if (label == ''){  /*a mensagem está vazia?*/
        texto = obter_texto(`Por favor, insira um texto de tamanho mínimo ${tamanho_minimo}!`)
    }else{
        texto = obter_texto(label)
    }
    if (len(label) < tamanho_minimo){/*tá no tamanho adequado?*/
        return obter_texto_tam_minimo()
    }
    return texto
}
export function obter_texto_tam_maximo(label,tamanho_maximo){
    if (label == ''){/*a mensagem está vazia?*/
        texto = obter_texto(`Por favor, insira um texto de tamanho mínimo ${tamanho_maximo}!`)
    }else{
        texto = obter_texto(label)
    }
    if (len(label) > tamanho_maximo){/*tá no tamanho adequado?*/
        return obter_texto_tam_maximo()
    }
    return texto
}

export function obter_texto_tam_min_maximo(label,tamanho_minimo, tamanho_maximo){
    if (label == ''){/*a mensagem está vazia?*/
        texto = obter_texto(`Por favor, insira um texto de tamanho mínimo ${tamanho_minimo} e de tamanho máx ${tamanho_maximo}!`)
    }
    else{
        texto = obter_texto(label)
    }
    if (tamanho_minimo > len(label) || len(label) > tamanho_maximo){
        return obter_texto_tam_min_maximo()
    }
    return texto
}

export function obter_opcoes(label, opcoes){}
    pass
/*===============================================================================================*/



/*1.1 INPUTS NUMÉRICOS*/
export function obter_numero(label='Digite um número{}'){
    numero = obter_texto(label)
    if (!eh_numero(numero)){
        return obter_numero(label)
    }
    return toNumber(numero)
}

export function obter_inteiro(label='Digite um inteiro{}'){}
    numero = obter_numero(label)
    if (! (eh_tipo_inteiro(numero))){}
        return obter_inteiro(label)
    return numero

export function obter_inteiro_positivo(label='Digite um inteiro positivo{} '){}
    numero = obter_numero(label)
    if !(eh_tipo_inteiro && numero > 0){}
        return obter_inteiro_positivo(label)
    return numero
    
export function obter_inteiro_negativo(label='Insira um inteiro negativo'){}
    numero = obter_numero(label)
    if !(eh_tipo_inteiro(numero) && numero < 0){}
        return obter_inteiro_positivo(label)
    return numero

export function obter_numero_minimo(tamanho_minimo,label=''){}
    if label == ''{}/*mensagem vazia?
        num = obter_numero(`f'`Por favor, digite um número maior ou igual a {tamanho_minimo}{} ')
    else{}
        num = obter_numero(label)
    if num < tamanho_minimo{}
        return obter_numero_minimo(label)
    return num
    
export function obter_numero_maximo(tamanho_maximo,label='Insira um número{} '){}
    if label == ''{}/*mensagem vazia?
        num = obter_numero(`f'`Por favor, digite um número menor ou igual a {tamanho_maximo}{} ')
    else{}
        num = obter_numero(label)
    if num > tamanho_maximo{}
        return obter_numero_maximo(label)
    return num
    
export function obter_numero_faixa(tamanho_minimo, tamanho_maximo,label='Insira um número{} '){}
    if label == ''{}/*mensagem vazia?
        num = obter_numero(`f'`Por favor, insira um número de ho mínimo {tamanho_minimo} e de máximo {tamanho_maximo}{} ')
    else{}
        num = obter_numero(label)
    if tamanho_minimo > num || num > tamanho_maximo{}
        return obter_numero_maximo(label)
    return num
/*===============================================================================================*/



/*2.MATEMATICA*/
export function eh_digito(string){
    for(let i = 0; i < 10 ; i++){
        if (string === str(i)){
            return true
        }
    }
    return false
}

export function eh_numero(string){
    let ha_nums = false
    let ha_um_ponto = false
    for (let i = 0; i < len(num); i++){
        if (eh_digito(string[i])){
            ha_nums = true
        } else if (eh_ponto(string[i])){
            if (ha_um_ponto){
                return false
            }
            ha_um_ponto = true
        }else{
            return false
        }
    }
    return ha_nums
}

export function toNumber(num){
    if (eh_numero(num)){
        return Number(num)
    }
    return num
}

export function eh_inteiro(num){
    if ((eh_numero(num)) && (! eh_float(num))){
        return true
    }
    return false
}

export function eh_tipo_inteiro(num){}
    return(type(num) == int)
        
export function divisores(num){}
    lista_divisores = []
    for i in range(1,num+1){}
        if num % i == 0{
            lista_divisores.push(i)
        }
    return lista_divisores

export function mmc(a,b){}
    ememc = a
    while (!(ememc % b == 0 && ememc % a == 0)){
        ememc += 1
    }
    return emedc
}

export function mdc(a,b){
    let emedc = a
    while (!(a % emedc == 0 && b % emedc == 0)){
        emedc -= 1
    }
    return emedc
}

export function eh_par(num){
    if(num % 2 == 0){
        return true
    }
    return false
}

export function eh_impar(num){
    if(num % 2 == 1){
        return true
    }
    return false
}

export function eh_primo(num){
    if (num < 0){
        return false}
    if (num === 0 || num === 1 || num === 2 || num === 3 || num === 5 || num === 7){
        return true
    }else if (num % 2 == 0 || num % 3 == 0 || num % 5 == 0 || num % 7 == 0){
        return false
    }
    return true
}

export function eh_numero_perfeito(num){}
    lista_divisores = divisores(num) 
    del(lista_divisores[-1])
    sum = 0
    for item in lista_divisores{}
        sum += item
    return (sum == num)

export function fatorial(num){}
    if (num == 1 || num == 0){
        return 1
    }
    return num * fatorial(num - 1)

export function raiz_quadrada(num){}
    return num ** (1/2)

export function raiz_cubica(num){}
    return num ** (1/3)

export function raiz(num,indice){}
    return num ** (1/indice)
/*===============================================================================================/*

/*3. STRINGS
export function juntar(string, separador=' '){} /*join
    new_string = ''
    for char in string{}
         if char != separador{}
            new_string += char
    return new_string

export function quebrar(stringa, separador=' '){} /*spllit
    new_string = ''
    string = stringa + separador
    lista = []
    for char in string{}
        if char != separador{}
            new_string += char
        else{}
            lista.append(new_string)
            new_string = ''
    return lista

export function quebrar_palavra(string){} /*spllit
    lista = []
    for char in string{}
        lista.append(char)
    return lista

export function mapear(funcao,colecao){
    if (typeof(colecao) === Array){
        const lista_modificada = Array
        for item in colecao{}
            lista_modificada.append(funcao(item))
        return lista_modificada
    elif type(colecao) == str{}
        string_modificada = ''
        for char in colecao{}
            string_modificada += funcao(char)
        return string_modificada
    '''elif type(colecao) == tuple{}
        lista_modificada = []
        for item in colecao{}
            lista_modificada.append(funcao(item))
        return tuple(lista_modificada)'''        
    return colecao
}


export function buscar(item,lista){
    for (elemento of lista){
        if (item === elemento){
            return true
        }
    }
    return false
}

export function filtrar(funcao_criterio,lista){} /*filter
    filtrados = []
    for item in lista{}
        if funcao_criterio(item){}
            filtrados.append(item)
    return filtrados

export function para_maiusculo(char){}
    if 97 <= ord(char) <= 122{}
        return chr(ord(char) - 32)
    return char

export function para_minusculo(char){}
    if 65 <= ord(char) <= 90{}
        return chr(ord(char) + 32)
    return char

export function eh_letra(char){}
    alfabeto = 'abcexport functionghijklmnopqrstuvwxyzABCexport functionGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,alfabeto)

export function eh_minuscula(char){
    const minusculas = 'abcdefghijklmnopqrstuvwxyz'
    return buscar(char,minusculas)
}

export function eh_maiuscula(char){
    const maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return buscar(char,maiusculas)
}

export function eh_ponto(char){
    return (char === '.')
}
export function eh_float(num){}
    for char in num{}
        if char == '.'{}
            return true
    return false

export function contar_ocorrencias_caractere(texto, caractere_buscado, ignore_caixa_alta_e_baixa){
    ocorrencias = 0
    if (ignore_caixa_alta_e_baixa){
        for (char of texto){
            if (char === para_maiusculo(caractere_buscado) || char == para_minusculo(caractere_buscado)){
                ocorrencias += 1
            }
        }
    } else if (ignore_caixa_alta_e_baixa === false){
        for (char of texto){
            if (char === caractere_buscado){
                ocorrencias += 1
            }
    }
    return ocorrencias
}
export function buscar_substring(string,substring){}
    tamanho = len(substring)
    for i in range(len(string)){}


'''export function eh_digito(num){}
    return (48 <= ord(num) <= 57)'''

