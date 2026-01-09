const numeros = [5, 50, 80, 1, 2, 3, 5, 8, 7, 11, 15, 22, 27]

const total = numeros.reduce(function(acumulador, valor) {
    acumulador += valor
    return acumulador
})
console.log(total)

const pares = numeros.reduce(function(acumulador, valor) {
    if (valor % 2 === 0) {
        acumulador.push(valor)
    }
    return acumulador
}, [])
console.log(pares)

const pessoas = [
    {nome: "Samuel", idade: 16},
    {nome: "Maria", idade: 23},
    {nome: "Eduardo", idade: 55},
    {nome: "Letícia", idade: 19},
    {nome: "Rosana", idade: 32},
    {nome: "Wallace", idade: 47}
]

const pessoa_mais_velha = pessoas.reduce(function(acumulador, valor) {
    if (acumulador.idade > valor.idade) {
        return acumulador
    }

    return valor
})
console.log(pessoa_mais_velha)