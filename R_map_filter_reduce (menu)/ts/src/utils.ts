import {question} from "readline-sync"

export function gerarMenu(titulo: string, opcoesIn: string) : string {

    const opcoes: string[] = opcoesIn.split(", ");

    let menu : string = `/***** ${titulo} *****\n|\n`;

    let i = 0;

    opcoes.forEach(

        function(elemento){

            i++;
            elemento.trim();
            menu += "| " + (i < 10 ? i : 0+i)
                + " - "+elemento+"\n";
        }
    ); 
    
    let star : string = "";

    for(let i = 0; i<titulo.length; i++){
        star += "*";
    }
    menu += `|\n| 0 - Sair\n\\***********${star}\n\nDigite sua escolha:`;

    return menu;
}

export function lerSimOuNao() : boolean{
  return question("Deseja passar um valor padrão? (0 - 1)\n>>> ") == "1";
}

export function limparConsole(): void {
    // Verifica se o ambiente é Node.js antes de tentar limpar o console
    if (typeof process !== 'undefined' && process.stdout.isTTY) {
      // Limpa o console no Node.js
      process.stdout.write('\x1Bc');
    } else {
      // Simula uma limpeza do console em outros ambientes
      console.clear();
    }
  }
  
  export function randint(min : number, max : number) : number {

    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  export function bye() {

    const byes : string[] = ["Tchauzinho!", "Até!", "Foi bom te ver!", "Beijo", "Cheiro"];
    return byes[randint(0,byes.length)];
  }