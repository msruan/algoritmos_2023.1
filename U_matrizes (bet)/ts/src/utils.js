"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.limparConsole = exports.gerarMenu = void 0;
function gerarMenu(titulo, opcoesIn) {
    var opcoes = opcoesIn.split(", ");
    var menu = "/***** ".concat(titulo, " *****\n|\n");
    var i = 0;
    opcoes.forEach(function (elemento) {
        i++;
        elemento.trim();
        menu += "| " + (i < 10 ? i : 0 + i)
            + " - " + elemento + "\n";
    });
    var star = "";
    for (var i_1 = 0; i_1 < titulo.length; i_1++) {
        star += "*";
    }
    menu += "|\n| 0 - Sair\n\\***********".concat(star, "\n\nDigite sua escolha:");
    return menu;
}
exports.gerarMenu = gerarMenu;
function limparConsole() {
    // Verifica se o ambiente é Node.js antes de tentar limpar o console
    if (typeof process !== 'undefined' && process.stdout.isTTY) {
        // Limpa o console no Node.js
        process.stdout.write('\x1Bc');
    }
    else {
        // Simula uma limpeza do console em outros ambientes
        console.clear();
    }
}
exports.limparConsole = limparConsole;
// Exemplo de uso
limparConsole();
