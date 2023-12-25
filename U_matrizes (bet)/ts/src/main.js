"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readline_sync_1 = require("readline-sync");
var utils_1 = require("./utils");
var feats = require("./features");
function main() {
    var SAIR = 0;
    var AUTO = 1;
    var MANUAL = 2;
    var ARRECADADO = 3;
    var SORTEIO = 4;
    var VENCEDORES = 5;
    var ZERAR = 6;
    var PRECO = parseFloat((0, readline_sync_1.question)("Digite o preço do bilhete: "));
    var menu;
    var escolha = -1;
    var bilhetes = [];
    var vencedores = [];
    var numsPremiados = [];
    do {
        console.log(bilhetes.length);
        menu = (0, utils_1.gerarMenu)("PatroBET", (numsPremiados.length < 1 ? "VENDA AUTO, VENDA MANUAL, " : "##########, ############, ")
            + (bilhetes.length > 0 ? "MOSTRAR ARRECADADO, " : "##################, ") +
            (numsPremiados.length < 6 && bilhetes.length > 0 ? "REALIZAR SORTEIO, " : "################, ") +
            (numsPremiados.length == 6 ? "MOSTRAR VENCEDORES," : "##################, ") + (bilhetes.length > 0 ? " ZERAR" : "#####"));
        escolha = parseInt((0, readline_sync_1.question)(menu));
        if (escolha == AUTO)
            bilhetes.push(feats.vendaAuto());
        else if (escolha == MANUAL)
            bilhetes.push(feats.vendaManual());
        else if (escolha == ARRECADADO)
            console.log("O arrecadado total é ", bilhetes.length * PRECO);
        else if (escolha == SORTEIO) {
            numsPremiados = feats.vendaAuto();
        }
        (0, utils_1.limparConsole)();
    } while (escolha != SAIR);
}
main();
