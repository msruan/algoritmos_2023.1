"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.vendaAuto = exports.vendaManual = void 0;
var readline_sync_1 = require("readline-sync");
function vendaManual() {
    var bilhete = new Array(6);
    for (var i = 0; i < 6; i++) {
        bilhete[i] = parseInt((0, readline_sync_1.question)("Digite o ".concat(i + 1, "\u00BA n\u00FAmero: ")));
        console.log();
    }
    return bilhete;
}
exports.vendaManual = vendaManual;
function vendaAuto() {
    var bilhete = new Array(6);
    for (var i = 0; i < 6; i++) {
        bilhete[i] = Math.floor(Math.random() * (60 - 1) + 1); //Math.random() * (max - min) + min;
    }
    return bilhete.sort();
}
exports.vendaAuto = vendaAuto;
