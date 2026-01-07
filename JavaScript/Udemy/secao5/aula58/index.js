const numeros = [5, 50, 80, 1, 2, 3, 5, 8, 7, 11, 15, 22, 27]

const numeros_dobrados = numeros.map(valor => valor * 2)

console.log(numeros_dobrados)

const pessoas = [
    {nome: "Samuel", idade: 16},
    {nome: "Maria", idade: 23},
    {nome: "Eduardo", idade: 55},
    {nome: "Letícia", idade: 19},
    {nome: "Rosana", idade: 32},
    {nome: "Wallace", idade: 47}
]

const nomes = pessoas.map(valor => valor.nome)
console.log(nomes)
const idades = pessoas.map(valor => valor.idade)
console.log(idades)
const pessoas_com_id = pessoas.map(function(valor, indice) {
    valor.id = indice
    return valor
})
console.log(pessoas_com_id)