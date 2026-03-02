import { nome as nome2, sobrenome, idade, soma, Pessoa } from "./modulo1.js"

const nome = "Oreki"

console.log(nome, nome2, sobrenome, idade)
console.log(soma(5, 5))

const pessoa = new Pessoa(nome2, sobrenome)
console.log(pessoa)